import threading

import numpy as np
from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog

import data
import database
import face
import servo
from failedfaceui import Ui_Dialog as Ui_FailedFaceWindow
from failedui import Ui_Dialog as Ui_FailedWindow
from indexui import Ui_MainWindow
from loadingui import Ui_Dialog as Ui_LoadingWindow
from pwdui import Ui_Dialog as Ui_PwdWindow
from unlockui import Ui_Dialog as Ui_UnlockWindow


def callFaceProcess():
    face.network()
    if data.method == 'capture' and data.online:
        database.updateCommand("status", 1, "none")
        tFace = threading.Thread(target=face.capture, args=())
        tFace.start()


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pwdPage = PwdWindow()
        self.loadingPage = LoadingWindows()
        self.unlockPage = UnlockWindows()
        self.failedPage = FailedWindows()
        self.failedFacePage = FailedFaceWindows()

        callFaceProcess()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camera_feed)
        self.timer.start(40)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.check_remote_command)
        self.timer2.start(3000)

    def pwdPressed(self):
        data.method = 'pwd'
        print('Goto password input page')
        data.pwd = ''
        self.pwdPage.showFullScreen()

    def update_camera_feed(self):
        if data.online:
            self.ui.cameraFeed.setPixmap(QPixmap.fromImage("images/waiting.jpg"))

            if type(data.cameraFeed) == np.ndarray and data.method == 'capture':
                image = QImage(data.cameraFeed, data.cameraFeed.shape[1], data.cameraFeed.shape[0],
                               data.cameraFeed.strides[0], QImage.Format_BGR888)
                image.scaled(640, 480)
                self.ui.cameraFeed.setPixmap(QPixmap.fromImage(image))
            elif data.method == 'baidu':
                self.timer.stop()
                result = face.baidu_api()

                print(result)

                if result != 'error':
                    self.unlockPage.showFullScreen()
                    unlockThread = threading.Thread(target=servo.unlock, args=())
                    unlockThread.start()
                    QTimer.singleShot(7000, lambda: self.unlockPage.close())
                    QTimer.singleShot(7000, lambda: callFaceProcess())
                    data.method = 'capture'
                else:
                    self.failedFacePage.showFullScreen()
                    QTimer.singleShot(3000, lambda: self.failedFacePage.close())
                    QTimer.singleShot(3000, lambda: callFaceProcess())
                    data.method = 'capture'

                self.timer.start(40)
                self.loadingPage.close()
            elif data.method == 'unlock':
                self.timer2.stop()
                database.updateCommand("status", 1, "none")
                self.unlockPage.showFullScreen()
                unlockThread = threading.Thread(target=servo.unlock, args=())
                unlockThread.start()
                QTimer.singleShot(7000, lambda: self.unlockPage.close())
                QTimer.singleShot(7000, lambda: callFaceProcess())
                data.method = 'capture'
                self.timer2.start(5000)
                self.loadingPage.close()

        else:
            self.ui.cameraFeed.setPixmap(QPixmap.fromImage("images/offline.jpg"))

    def check_remote_command(self):
        command = database.fetch_all("status")[1][3]
        print(command)
        if command == "unlock":
            data.method = 'unlock'


class PwdWindow(QDialog):
    def __init__(self):
        super(PwdWindow, self).__init__()
        self.failedPage = FailedWindows()
        self.unlockPage = UnlockWindows()
        self.ui = Ui_PwdWindow()
        self.ui.setupUi(self)

    def passwordInput(self, i):
        if type(i) == int and len(data.pwd) < 6:
            data.pwd += str(i)
            if len(data.pwd) == 6:
                i = 'yes'
        if i == 'yes' and len(data.pwd) > 0:
            if data.pwd == '123456':
                self.unlockPage.showFullScreen()
                data.pwd = ''
                unlockThread = threading.Thread(target=servo.unlock, args=())
                unlockThread.start()
                QTimer.singleShot(7000, lambda: self.unlockPage.close())
                QTimer.singleShot(7000, lambda: callFaceProcess())
                data.method = 'capture'
                self.close()

            else:
                self.failedPage.showFullScreen()
                data.pwd = ''

        elif i == 'back' and len(data.pwd) > 0:
            data.pwd = data.pwd[:-1]

        self.ui.textEdit.setText(data.pwd)

    def backfrompwd(self):
        data.method = 'capture'
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
        self.ui = Ui_FailedWindow()
        self.ui.setupUi(self)


class LoadingWindows(QDialog):
    def __init__(self):
        super(LoadingWindows, self).__init__()
        self.ui = Ui_LoadingWindow()
        self.ui.setupUi(self)


class FailedFaceWindows(QDialog):
    def __init__(self):
        super(FailedFaceWindows, self).__init__()
        self.ui = Ui_FailedFaceWindow()
        self.ui.setupUi(self)


def init():
    app = QApplication()
    windows = MainWindows()
    windows.showFullScreen()

    app.exec_()
