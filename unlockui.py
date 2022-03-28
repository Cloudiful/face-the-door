# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unlockPage.ui'
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
        self.label.setGeometry(QRect(170, 170, 471, 131))
        font = QFont()
        font.setFamily(u"\u841d\u8389\u4f53")
        font.setPointSize(28)
        self.label.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Unlock", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6210\u529f\u89e3\u9501\uff0c\u8bf7\u5728\u4e94\u79d2\u5185\u8fdb\u5165", None))
    # retranslateUi

