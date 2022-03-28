from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
import data
from indexui import Ui_MainWindow
from pwdui import Ui_Dialog as Ui_PwdWindow
from unlockui import Ui_Dialog as Ui_UnlockWindow


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

    def passwordInput(self, i):
        if len(data.pwd) < 6:
            if type(i) == int:
                data.pwd += str(i)
            elif i == 'yes':
                pass
            elif i == 'back' and len(data.pwd) > 0:
                data.pwd = data.pwd[:-1]

        self.ui.textEdit.setText(data.pwd)

    def b0(self):
        self.passwordInput(0)

    def b1(self):
        self.passwordInput(1)

    def b2(self):
        self.passwordInput(2)

    def b3(self):
        self.passwordInput(3)

    def b4(self):
        self.passwordInput(4)

    def b5(self):
        self.passwordInput(5)

    def b6(self):
        self.passwordInput(6)

    def b7(self):
        self.passwordInput(7)

    def b8(self):
        self.passwordInput(8)

    def b9(self):
        self.passwordInput(9)

    def byes(self):
        self.passwordInput('yes')

    def bback(self):
        self.passwordInput('back')


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
