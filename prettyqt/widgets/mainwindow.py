# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from typing import Dict

import qtawesome as qta
from qtpy import QtCore, QtWidgets

from prettyqt import widgets

DOCK_POSITIONS = dict(top=QtCore.Qt.TopDockWidgetArea,
                      bottom=QtCore.Qt.BottomDockWidgetArea,
                      left=QtCore.Qt.LeftDockWidgetArea,
                      right=QtCore.Qt.RightDockWidgetArea)


class MainWindow(QtWidgets.QMainWindow):
    """
    Class for our mainWindow
    includes all docks, a centralwidget and a toolbar
    """

    # def load_window_state(self):
    #     prefix = os.environ["QT_API"]
    #     geom = application.settings.get(f"{prefix}.geometry", self.saveGeometry())
    #     state = application.settings.get(f"{prefix}.state", self.saveState())
    #     self.restoreGeometry(geom)
    #     self.restoreState(state)

    # def closeEvent(self, event):
    #     """
    #     override, gets executed when app gets closed.
    #     saves GUI settings
    #     """
    #     prefix = os.environ["QT_API"]
    #     application.settings[f"{prefix}.geometry"] = self.saveGeometry()
    #     application.settings[f"{prefix}.state"] = self.saveState()
    #     super().closeEvent(event)
    #     event.accept()

    def set_icon(self, icon):
        if icon:
            if isinstance(icon, str):
                icon = qta.icon(icon, color="lightgray")
            self.setWindowIcon(icon)

    def set_stylesheet(self, item, dct: Dict[str, str]) -> str:
        ss = "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in dct.items())
        self.setStyleSheet(f"{item} {{{ss};}}")

    def add_dockwidget(self,
                       name: str,
                       title: str,
                       vertical: bool = True,
                       position: str = "left") -> widgets.DockWidget:
        dock_widget = widgets.DockWidget(self, name=name, title=title)
        widget = widgets.Widget()
        widget.setObjectName(f"{name}.widget")
        if vertical:
            layout = QtWidgets.QVBoxLayout(widget)
        else:
            layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        dock_widget.setWidget(widget)
        position = DOCK_POSITIONS[position]
        self.addDockWidget(QtCore.Qt.DockWidgetArea(position), dock_widget)
        dock_widget.layout = layout
        return dock_widget

    def toggle_fullscreen(self):
        """toggle between fullscreen and regular size
        """
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


if __name__ == "__main__":
    app = widgets.Application.create_default_app()
    form = MainWindow()
    form.show()
    app.exec_()
