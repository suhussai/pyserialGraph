# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Dec  7 22:54:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(634, 429)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label)
        self.portName = QtGui.QLineEdit(self.centralwidget)
        self.portName.setObjectName(_fromUtf8("portName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.portName)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_2)
        self.btnListen = QtGui.QPushButton(self.centralwidget)
        self.btnListen.setObjectName(_fromUtf8("btnListen"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.btnListen)
        self.fieldDisplay = QtGui.QListWidget(self.centralwidget)
        self.fieldDisplay.setObjectName(_fromUtf8("fieldDisplay"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.fieldDisplay)
        self.baudRate = QtGui.QLineEdit(self.centralwidget)
        self.baudRate.setObjectName(_fromUtf8("baudRate"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.baudRate)
        self.btnShutdown = QtGui.QPushButton(self.centralwidget)
        self.btnShutdown.setObjectName(_fromUtf8("btnShutdown"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.btnShutdown)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Port Name", None))
        self.label_2.setText(_translate("MainWindow", "Baud Rate", None))
        self.btnListen.setText(_translate("MainWindow", "Listen", None))
        self.btnShutdown.setText(_translate("MainWindow", "ShutDown", None))

