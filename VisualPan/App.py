from VisualPan.Core.version import *
from PySide2.QtWidgets import QMainWindow


def winTitle():
    return "VisualPan v{0}".format(currentVersion().__str__())


# app itself
class VisualPan(QMainWindow):

    def __init__(self, parent=None):
        super(VisualPan, self).__init__(parent=parent)
        self.setWindowTitle(winTitle())

    @staticmethod
    def instance(parent=None):
        instance = VisualPan(parent)
