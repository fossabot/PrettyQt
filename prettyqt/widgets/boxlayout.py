# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy import QtCore, QtWidgets

MODES = dict(maximum=QtWidgets.QLayout.SetMaximumSize,
             fixed=QtWidgets.QLayout.SetFixedSize)

ALIGNMENTS = dict(left=QtCore.Qt.AlignLeft,
                  right=QtCore.Qt.AlignRight,
                  top=QtCore.Qt.AlignTop,
                  bottom=QtCore.Qt.AlignBottom)


class BoxLayout(QtWidgets.QBoxLayout):

    def __init__(self, orientation, parent=None):
        o = self.TopToBottom if orientation == "vertical" else self.LeftToRight
        super().__init__(o, parent)
        self.setContentsMargins(0, 0, 0, 0)

    def __getitem__(self, index):
        return self.itemAt(index)

    def __len__(self):
        return self.count()

    def set_size_mode(self, mode: str):
        if mode not in MODES:
            raise ValueError(f"{mode} not a valid size mode.")
        self.setSizeConstraint(MODES[mode])

    def set_alignment(self, alignment: str):
        if alignment not in ALIGNMENTS:
            raise ValueError(f"{alignment} not a valid alignment.")
        self.setAlignment(ALIGNMENTS[alignment])


if __name__ == "__main__":
    from prettyqt import widgets
    app = widgets.Application.create_default_app()
    layout = BoxLayout("vertical")
    widget = widgets.Widget()
    widget.setLayout(layout)
    widget.show()
    app.exec_()
