import pwdui
import face
import servo
import threading
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
import data
from indexui import Ui_MainWindow
from pwdui import Ui_Dialog as Ui_PwdWindow
from unlockui import Ui_Dialog as Ui_UnlockWindow
from failedui import Ui_Dialog as Ui_FailedWindows


def callFaceProcess():
    if data.method == 'face':
        tFace = threading.Thread(target=face.capture, args=())
        tFace.start()


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pwdPage = None
        callFaceProcess()

    def pwdPressed(self):
        data.method = 'pwd'
        print('Goto password input page')
        data.pwd = ''
        self.pwdPage = PwdWindow()
        self.pwdPage.showFullScreen()


class PwdWindow(QDialog):
    def __init__(self):
        super(PwdWindow, self).__init__()
        self.failedPage = None
        self.unlockPage = None
        self.ui = Ui_PwdWindow()
        self.ui.setupUi(self)

    def passwordInput(self, i):
        if type(i) == int and len(data.pwd) < 6:
            data.pwd += str(i)
        elif i == 'yes':
            if data.pwd == '123456':
                self.unlockPage = UnlockWindows()
                self.unlockPage.showFullScreen()
                data.pwd = ''
                unlockThread = threading.Thread(target=servo.unlock, args=())
                unlockThread.start()
                pwdui.QTimer.singleShot(7000, lambda: self.unlockPage.close())

                data.method = 'face'
                callFaceProcess()
                self.close()

            else:
                self.failedPage = FailedWindows()
                self.failedPage.showFullScreen()
                data.pwd = ''

        elif i == 'back' and len(data.pwd) > 0:
            data.pwd = data.pwd[:-1]

        self.ui.textEdit.setText(data.pwd)

    def backfrompwd(self):
        data.method = 'face'
        callFaceProcess()
        self.close()

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

    def back(self):
        self.passwordInput('back')


class UnlockWindows(QDialog):
    def __init__(self):
        super(UnlockWindows, self).__init__()
        self.ui = Ui_UnlockWindow()
        self.ui.setupUi(self)


class FailedWindows(QDialog):
    def __init__(self):
        super(FailedWindows, self).__init__()
        self.ui = Ui_FailedWindows()
        self.ui.setupUi(self)


def init():
    app = QApplication()
    windows = MainWindows()
    windows.showFullScreen()

    app.exec_()
