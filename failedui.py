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
        Dialog.setWindowOpacity(0.900000000000000)
        Dialog.setAutoFillBackground(True)
        self.text = QLabel(Dialog)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(260, 80, 261, 111))
        font = QFont()
        font.setFamily(u"\u841d\u8389\u4f53")
        font.setPointSize(48)
        self.text.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 240, 341, 151))
        self.pushButton.setFont(font)

        self.retranslateUi(Dialog)
        self.pushButton.released.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Failed", None))
        self.text.setText(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u5931\u8d25", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u91cd\u8bd5", None))
    # retranslateUi

