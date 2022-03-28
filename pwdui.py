# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pwdPage.ui'
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
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 200, 331, 81))
        font = QFont()
        font.setFamily(u"\u841d\u8389\u4f53")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 20, 141, 71))
        font1 = QFont()
        font1.setFamily(u"\u841d\u8389\u4f53")
        font1.setPointSize(28)
        self.pushButton_7.setFont(font1)
        self.b2 = QPushButton(Dialog)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(530, 30, 100, 100))
        font2 = QFont()
        font2.setFamily(u"\u841d\u8389\u4f53")
        font2.setPointSize(36)
        self.b2.setFont(font2)
        self.b9 = QPushButton(Dialog)
        self.b9.setObjectName(u"b9")
        self.b9.setGeometry(QRect(630, 230, 100, 100))
        self.b9.setFont(font2)
        self.b0 = QPushButton(Dialog)
        self.b0.setObjectName(u"b0")
        self.b0.setGeometry(QRect(530, 330, 100, 100))
        self.b0.setFont(font2)
        self.b7 = QPushButton(Dialog)
        self.b7.setObjectName(u"b7")
        self.b7.setGeometry(QRect(430, 230, 100, 100))
        self.b7.setFont(font2)
        self.b1 = QPushButton(Dialog)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(430, 30, 100, 100))
        self.b1.setFont(font2)
        self.b1.setAutoFillBackground(False)
        self.b1.setCheckable(False)
        self.b6 = QPushButton(Dialog)
        self.b6.setObjectName(u"b6")
        self.b6.setGeometry(QRect(630, 130, 100, 100))
        self.b6.setFont(font2)
        self.b4 = QPushButton(Dialog)
        self.b4.setObjectName(u"b4")
        self.b4.setGeometry(QRect(430, 130, 100, 100))
        self.b4.setFont(font2)
        self.bb = QPushButton(Dialog)
        self.bb.setObjectName(u"bb")
        self.bb.setGeometry(QRect(630, 330, 100, 100))
        font3 = QFont()
        font3.setFamily(u"\u841d\u8389\u4f53")
        font3.setPointSize(22)
        self.bb.setFont(font3)
        self.b8 = QPushButton(Dialog)
        self.b8.setObjectName(u"b8")
        self.b8.setGeometry(QRect(530, 230, 100, 100))
        self.b8.setFont(font2)
        self.b5 = QPushButton(Dialog)
        self.b5.setObjectName(u"b5")
        self.b5.setGeometry(QRect(530, 130, 100, 100))
        self.b5.setFont(font2)
        self.by = QPushButton(Dialog)
        self.by.setObjectName(u"by")
        self.by.setGeometry(QRect(430, 330, 100, 100))
        self.by.setFont(font3)
        self.b3 = QPushButton(Dialog)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(630, 30, 100, 100))
        self.b3.setFont(font2)
        QWidget.setTabOrder(self.textEdit, self.pushButton_7)

        self.retranslateUi(Dialog)
        self.pushButton_7.released.connect(Dialog.close)
        self.b1.released.connect(Dialog.b1)
        self.b2.released.connect(Dialog.b2)
        self.b3.released.connect(Dialog.b3)
        self.b4.released.connect(Dialog.b4)
        self.b5.released.connect(Dialog.b5)
        self.b6.released.connect(Dialog.b6)
        self.b7.released.connect(Dialog.b7)
        self.b8.released.connect(Dialog.b8)
        self.b9.released.connect(Dialog.b9)
        self.by.released.connect(Dialog.byes)
        self.bb.released.connect(Dialog.bback)
        self.b0.released.connect(Dialog.b0)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u841d\u8389\u4f53'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de", None))
        self.b2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.b9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.b0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.b7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.b1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.b6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.b4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.bb.setText(QCoreApplication.translate("Dialog", u"\u9000\u683c", None))
        self.b8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.b5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.by.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.b3.setText(QCoreApplication.translate("Dialog", u"3", None))
    # retranslateUi

