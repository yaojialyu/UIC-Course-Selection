# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Jul 09 20:17:30 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class MIS_GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtGui.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 100, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 130, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 90, 151, 51))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuHello_world = QtGui.QMenu(self.menuBar)
        self.menuHello_world.setObjectName("menuHello_world")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuHello_world.addAction(self.action)
        self.menuBar.addAction(self.menuHello_world.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "你好", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">哈哈哈哈哈哈哈哈</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHello_world.setTitle(QtGui.QApplication.translate("MainWindow", "hello world", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("MainWindow", "你好", None, QtGui.QApplication.UnicodeUTF8))

