from PySide2.QtWidgets import QApplication, QMainWindow, QDialog

from indexui import Ui_MainWindow
from pwdui import Ui_Dialog as Ui_PwdWindow
from unlockui import Ui_Dialog as Ui_UnlockWindow

password = ''


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pwdPage = None

    def pwdPressed(self):
        print('Goto password input page')
        self.pwdPage = PwdWindow()
        self.pwdPage.showFullScreen()


class PwdWindow(QDialog):
    def __init__(self):
        super(PwdWindow, self).__init__()
        self.ui = Ui_PwdWindow()
        self.ui.setupUi(self)


class UnlockWindows(QDialog):
    def __init__(self):
        super(UnlockWindows, self).__init__()
        self.ui = Ui_UnlockWindow
        self.ui.setupUi(self)


def init():
    app = QApplication()
    windows = MainWindows()
    windows.showFullScreen()

    app.exec_()
