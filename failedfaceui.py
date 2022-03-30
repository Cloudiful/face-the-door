# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'failedPageFace.ui'
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
        self.text = QLabel(Dialog)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(160, 170, 451, 181))
        font = QFont()
        font.setFamily(u"\u841d\u8389\u4f53")
        font.setPointSize(48)
        self.text.setFont(font)
        self.text.setTextFormat(Qt.PlainText)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.text.setText(QCoreApplication.translate("Dialog", u"     \u8bc6\u522b\u5931\u8d25\n"
"   \u8bf7\u7a0d\u540e\u91cd\u8bd5", None))
    # retranslateUi

