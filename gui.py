from PySide2.QtWidgets import QApplication, QMainWindow
from indexui import Ui_MainWindow
from pwdui import Ui_MainWindow as Ui_PwdWindow
from unlockui import Ui_MainWindow as Ui_UnlockWindows


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.pwdWindow = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def pwdPressed(self):
        print('pressed!')
        self.pwdWindow = PwdWindow()
        self.pwdWindow.showFullScreen()


class PwdWindow(QMainWindow):
    def __init__(self):
        super(PwdWindow, self).__init__()
        self.ui = Ui_PwdWindow()
        self.ui.setupUi(self)


class UnlockWindows(QMainWindow):
    def __init__(self):
        super(UnlockWindows, self).__init__()
        self.ui = Ui_UnlockWindows
        self.ui.setupUi(self)


app = QApplication()
windows = MainWindows()
windows.showFullScreen()

app.exec_()
