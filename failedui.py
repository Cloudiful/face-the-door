# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'failedPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 480)
        Dialog.setWindowOpacity(1.000000000000000)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 150, 151, 51))
        font = QFont()
        font.setFamily(u"\u841d\u8389\u4f53")
        font.setPointSize(28)
        self.label.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 300, 271, 131))
        font1 = QFont()
        font1.setFamily(u"\u841d\u8389\u4f53")
        font1.setPointSize(26)
        self.pushButton.setFont(font1)

        self.retranslateUi(Dialog)
        self.pushButton.released.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Failed", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801\u9519\u8bef\uff01", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u91cd\u8bd5", None))
    # retranslateUi

