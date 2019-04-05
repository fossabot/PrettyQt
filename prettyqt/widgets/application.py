# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from typing import Optional
from qtpy import QtWidgets, QtCore
import qtawesome as qta


class Application(QtWidgets.QApplication):

    def set_icon(self, icon):
        if icon:
            if isinstance(icon, str):
                icon = qta.icon(icon, color="lightgray")
            self.setWindowIcon(icon)

    def load_language_file(self, path):
        translator = QtCore.QTranslator(self)
        translator.load(str(path))
        self.installTranslator(translator)

    def set_metadata(self,
                     app_name: Optional[str] = None,
                     app_version: Optional[str] = None,
                     org_name: Optional[str] = None,
                     org_domain: Optional[str] = None):
        if app_name:
            self.setApplicationName(app_name)
        if app_version:
            self.setApplicationVersion(app_name)
        if org_name:
            self.setOrganizationName(org_name)
        if org_domain:
            self.setOrganizationDomain(org_domain)

    @classmethod
    def use_hdpi_bitmaps(cls):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    @classmethod
    def disable_window_help_button(cls):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_DisableWindowContextHelpButton)

    @classmethod
    def copy_to_clipboard(cls, text: str):
        """
        Sets clipboard to supplied text
        """
        cb = cls.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(text, mode=cb.Clipboard)

    @classmethod
    def get_mainwindow(cls):
        widget_list = cls.instance().topLevelWidgets()
        for widget in widget_list:
            if isinstance(widget, QtWidgets.QMainWindow):
                return widget
