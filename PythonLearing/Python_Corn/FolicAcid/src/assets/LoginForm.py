# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(459, 137)
        self.usrLabel = QtWidgets.QLabel(LoginForm)
        self.usrLabel.setGeometry(QtCore.QRect(260, 20, 41, 16))
        self.usrLabel.setObjectName("usrLabel")
        self.psdLabel = QtWidgets.QLabel(LoginForm)
        self.psdLabel.setGeometry(QtCore.QRect(260, 60, 41, 16))
        self.psdLabel.setObjectName("psdLabel")
        self.loginBtn = QtWidgets.QPushButton(LoginForm)
        self.loginBtn.setGeometry(QtCore.QRect(260, 100, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        self.exitBtn = QtWidgets.QPushButton(LoginForm)
        self.exitBtn.setGeometry(QtCore.QRect(370, 100, 75, 23))
        self.exitBtn.setObjectName("exitBtn")
        self.loginResultText = QtWidgets.QTextEdit(LoginForm)
        self.loginResultText.setGeometry(QtCore.QRect(40, 30, 161, 71))
        self.loginResultText.setObjectName("loginResultText")
        self.usrText = QtWidgets.QLineEdit(LoginForm)
        self.usrText.setGeometry(QtCore.QRect(310, 20, 133, 20))
        self.usrText.setObjectName("usrText")
        self.psdText = QtWidgets.QLineEdit(LoginForm)
        self.psdText.setGeometry(QtCore.QRect(310, 60, 133, 20))
        self.psdText.setObjectName("psdText")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "登陆"))
        self.usrLabel.setText(_translate("LoginForm", "用户名"))
        self.psdLabel.setText(_translate("LoginForm", "密  码"))
        self.loginBtn.setText(_translate("LoginForm", "登陆"))
        self.exitBtn.setText(_translate("LoginForm", "退出"))

