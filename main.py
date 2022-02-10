__author__ = "Lukas Mahler"
__version__ = "0.0.0"
__date__ = "10.02.2022"
__email__ = "m@hler.eu"
__status__ = "Development"


try:
    # Defaults
    import os
    import sys

    # Ui
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import Qt
    from ui.main import Ui_Main

    # Self
    from src import util

except ImportError as e:
    print(f"ERROR: Missing Module [{e}]")
    sys.exit()


class QTInstance(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # disable windows default window buttons
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # remove not filled background
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)

    def btnexit(self):
        self.destroy()
        sys.exit(app.exec_())

    def status(self, txt):
        self.statusbar.showMessage(txt)


def preload():

    # Load toml config
    global config
    config = util.getConf("settings.toml")


if __name__ == "__main__":

    preload()
    app = QtWidgets.QApplication(sys.argv)
    window = QTInstance()
    window.show()

    sys.exit(app.exec_())

