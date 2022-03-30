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
        font = QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pwdButton = QPushButton(self.centralwidget)
        self.pwdButton.setObjectName(u"pwdButton")
        self.pwdButton.setGeometry(QRect(640, 50, 161, 431))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwdButton.sizePolicy().hasHeightForWidth())
        self.pwdButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"\u841d\u8389\u4f53")
        font1.setPointSize(42)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.pwdButton.setFont(font1)
        self.pwdButton.setAcceptDrops(False)
        self.pwdButton.setAutoFillBackground(True)
        self.pwdButton.setCheckable(False)
        self.pwdButton.setAutoRepeatInterval(0)
        self.pwdButton.setAutoDefault(False)
        self.pwdButton.setFlat(True)
        self.cameraFeed = QLabel(self.centralwidget)
        self.cameraFeed.setObjectName(u"cameraFeed")
        self.cameraFeed.setGeometry(QRect(0, 0, 640, 480))
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei")
        self.cameraFeed.setFont(font2)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(670, 10, 111, 31))
        font3 = QFont()
        font3.setFamily(u"\u841d\u8389\u4f53")
        font3.setPointSize(16)
        self.label.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.cameraFeed.raise_()
        self.pwdButton.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)
        self.pwdButton.released.connect(MainWindow.pwdPressed)

        self.pwdButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pwdButton.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\n"
"\u7801\n"
"\u89e3\n"
"\u9501", None))
        self.cameraFeed.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6216 \u8005 \u4f7f \u7528", None))
    # retranslateUi

