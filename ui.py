# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cameraFeed = QLabel(self.centralwidget)
        self.cameraFeed.setObjectName(u"cameraFeed")
        self.cameraFeed.setGeometry(QRect(0, 0, 800, 480))
        font = QFont()
        font.setFamily(u"\u841d\u8389\u4f53")
        font.setPointSize(14)
        self.cameraFeed.setFont(font)
        self.cameraFeed.setMouseTracking(False)
        self.pwdButton = QPushButton(self.centralwidget)
        self.pwdButton.setObjectName(u"pwdButton")
        self.pwdButton.setGeometry(QRect(250, 330, 281, 91))
        font1 = QFont()
        font1.setFamily(u"\u841d\u8389\u4f53")
        font1.setPointSize(36)
        self.pwdButton.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cameraFeed.setText(QCoreApplication.translate("MainWindow", u"cameraFeed", None))
        self.pwdButton.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\u89e3\u9501", None))
    # retranslateUi

