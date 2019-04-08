from PyQt5.QtWidgets import QDialog
import sys
import os

sys.path.append(os.path.abspath('../gui'))
from Ui_AboutDialog import Ui_About


class AboutDialog(QDialog, Ui_About):

    def __init__(self):
        super(AboutDialog, self).__init__()

        self.setupUi(self)
        self.textEdit.setReadOnly(True)
