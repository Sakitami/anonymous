# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sakitami\工作\学习\匿名信\userinterface\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 370)
        MainWindow.setMinimumSize(QtCore.QSize(590, 370))
        MainWindow.setMaximumSize(QtCore.QSize(590, 370))
        MainWindow.setSizeIncrement(QtCore.QSize(590, 370))
        MainWindow.setBaseSize(QtCore.QSize(590, 370))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 571, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 551, 131))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 231, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 99, 251, 21))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 251, 71))
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 150, 551, 131))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_6)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 231, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_13.addWidget(self.lineEdit_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_6.addWidget(self.pushButton_9)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_6)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 20, 229, 101))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_16.addWidget(self.label_11)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_16.addWidget(self.lineEdit_7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_10.addWidget(self.lineEdit_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_17.addWidget(self.lineEdit_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_10.addWidget(self.pushButton_10)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 541, 291))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_8)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_11.addWidget(self.listWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView_3 = QtWidgets.QTableView(self.tab_3)
        self.tableView_3.setEnabled(False)
        self.tableView_3.setGeometry(QtCore.QRect(10, 10, 541, 261))
        self.tableView_3.setObjectName("tableView_3")
        self.letterlist=QtGui.QStandardItemModel()
        self.letterlist.setHorizontalHeaderLabels(['发件人','是否已读','发件时间','清除时间'])
        self.tableView_3.setModel(self.letterlist)
        self.tableView_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_3.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 270, 320, 41))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_12.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_12.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_12.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_12.addWidget(self.pushButton_8)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_12.addWidget(self.pushButton_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableView_4 = QtWidgets.QTableView(self.tab_7)
        self.tableView_4.setEnabled(False)
        self.tableView_4.setGeometry(QtCore.QRect(10, 10, 541, 261))
        self.tableView_4.setObjectName("tableView_4")
        self.sendlist=QtGui.QStandardItemModel()
        self.sendlist.setHorizontalHeaderLabels(['收件人','是否已读','发件时间','清除时间'])
        self.tableView_4.setModel(self.sendlist)
        self.tableView_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_4.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_4.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.tab_7)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 270, 320, 41))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_19.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_19.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_19.addWidget(self.pushButton_14)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_19.addWidget(self.pushButton_4)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(10, 10, 541, 31))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_14)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_14.addWidget(self.lineEdit_6)
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(10, 40, 541, 31))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_15)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_15)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_15.addWidget(self.comboBox_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 541, 211))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 280, 101, 31))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(450, 280, 101, 31))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_8.addWidget(self.pushButton_3)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(110, 280, 101, 31))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget_7)
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout_9.addWidget(self.dateTimeEdit)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 541, 151))
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 521, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_3.addWidget(self.lineEdit_10)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 521, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_7.addWidget(self.lineEdit_9)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 521, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_8.addWidget(self.lineEdit_11)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 110, 521, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_18.addWidget(self.lineEdit_12)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 10, 561, 101))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_6)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 431, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 110, 561, 191))
        self.groupBox_7.setObjectName("groupBox_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_7)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 561, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_6, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 345, 571, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "概览"))
        self.label_2.setText(_translate("MainWindow", "用户ID:"))
        self.label_3.setText(_translate("MainWindow", "未登录"))
        self.label_4.setText(_translate("MainWindow", "状态:"))
        self.label_5.setText(_translate("MainWindow", "离线"))
        self.groupBox_2.setTitle(_translate("MainWindow", "匿名名片"))
        self.pushButton.setText(_translate("MainWindow", "添加/删除"))
        self.groupBox_3.setTitle(_translate("MainWindow", "登录"))
        self.label_10.setText(_translate("MainWindow", "用户ID:"))
        self.label_9.setText(_translate("MainWindow", "密码:  "))
        self.pushButton_9.setText(_translate("MainWindow", "登录"))
        self.groupBox_4.setTitle(_translate("MainWindow", "注册"))
        self.label_11.setText(_translate("MainWindow", "用户ID:"))
        self.label_14.setText(_translate("MainWindow", "密码:  "))
        self.label_15.setText(_translate("MainWindow", "确认:  "))
        self.pushButton_10.setText(_translate("MainWindow", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "状态"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "用户列表"))
        self.tableView_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "标记已读"))
        self.pushButton_6.setText(_translate("MainWindow", "删除信件"))
        self.pushButton_7.setText(_translate("MainWindow", "双向删除"))
        self.pushButton_8.setText(_translate("MainWindow", "查看信件"))
        self.pushButton_2.setText(_translate("MainWindow", "手动刷新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "我的信件"))
        self.tableView_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_12.setText(_translate("MainWindow", "删除信件"))
        self.pushButton_13.setText(_translate("MainWindow", "双向删除"))
        self.pushButton_14.setText(_translate("MainWindow", "查看信件"))
        self.pushButton_4.setText(_translate("MainWindow", "手动刷新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "已发信件"))
        self.label_12.setText(_translate("MainWindow", "To:"))
        self.label_13.setText(_translate("MainWindow", "By:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1天"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3天"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10天"))
        self.comboBox.setItemText(3, _translate("MainWindow", "1月"))
        self.comboBox.setItemText(4, _translate("MainWindow", "不清除"))
        self.pushButton_3.setText(_translate("MainWindow", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "发送信件"))
        self.groupBox_5.setTitle(_translate("MainWindow", "指定服务器"))
        self.label_6.setText(_translate("MainWindow", "数据库地址："))
        self.label_8.setText(_translate("MainWindow", ":"))
        self.label_7.setText(_translate("MainWindow", "数据库名："))
        self.label_16.setText(_translate("MainWindow", "用户名："))
        self.label_17.setText(_translate("MainWindow", "密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "设置"))
        self.groupBox_6.setTitle(_translate("MainWindow", "关于"))
        self.label_21.setText(_translate("MainWindow", "匿名信 Anonymous"))
        self.label_22.setText(_translate("MainWindow", "版本： DEMO-v0.0.2"))
        self.label_18.setText(_translate("MainWindow", "项目地址：https://github.com/Sakitami/anonymous"))
        self.label_19.setText(_translate("MainWindow", "作者：Sakitami"))
        self.label_20.setText(_translate("MainWindow", "E-mail:sakitami@mail.tust.edu.cn"))
        self.groupBox_7.setTitle(_translate("MainWindow", "使用许可"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">匿名信 软件最终用户许可协议  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">重要须知━请认真阅读：本《最终用户许可协议》（以下称《协议》）是您（单一实体）与 匿名信之间有关上述匿名信软件产品的法律协议。   </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本软件包括计算机软件，并可能包括相关媒体、印刷材料和“联机”或电子文档（“软件产品”）。本软件还包括对匿名信提供给您的原软件的任何更新和补充资料。任何与本软件一同提供给您的并与单独一份最终用户许可证相关的软件产品是根据那份许可协议中的条款而授予您。您一旦安装、复制、下载、访问或以其它方式使用软件，即表示您同意接受本《协议》各项条款的约束。如您不同意本《协议》中的条款，请不要安装或使用该软件；但您可将其退回原购买处，并获得全额退款。 软件产品许可证  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本“软件产品”受袒护著作权法及国际著作权条约和其它知识产权法和条约的保护。本“软件产品”只许可使用，而不出售。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1．许可证的授予。本《协议》授予您下列权利： </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．应用软件。您可在单一一台计算机上安装、使用、访问、显示、运行或以其它方式互相作用于（“运行”）本软件（或适用于同一操作系统的任何前版本）的一份副本。运行的计算机的主要用户可以制作另一份副本，仅供在其在安装到公司其他电脑管理注册后的同一项目之用。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．储存／网络用途。您还可以在您公司的其它计算机上运行软件但仅限于注册时所添之项目，您必须为增加的每个项目获得一份许可证。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．保留权利。未明示授予的一切其它权利均为Sakitami个人所有。 </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2．其它权利和限制的说明。   </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．试用版本。仅限于试用，如需正式使用，必须注册成为正式版。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．组件的分隔。本“软件产品”是作为单一产品而被授予使用许可的。您不得将其组成部分分开在多台计算机上使用。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．商标。本《协议》不授予您有关任何匿名信商标或服务商标的任何权利。   </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．出租。不得出租、租赁或出借本软件。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．支持服务。xxx有限公司可能为您提供与“软件产品”有关的支持服务。支持服务的使用受用户手册、联机文档和/或其它提供的材料中所述的各项政策和计划的制约。提供给您作为支持服务的一部份的任何附加软件代码应被视为本软件的一部分，并须符合本《协议》中的各项条款和条件。至于您提供给Sakitami作为支持服务的一部分的技术信息，Sakitami可将其用于商业用途，包括产品支持和开发。 </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．软件转让。本软件的第一被许可人不可以对本《协议》及本软件直接或间接向任何用户作转让。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">．终止。如您未遵守本《协议》的各项条款和条件，在不损害其它权利的情况下，Sakitami可终止本《协议》。如此类情况发生，您必须销毁“软件产品”的所有副本及其所有组成部分。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3．升级版本。如本软件标明为升级版本，您必须获取Sakitami标明为合格使用升级版本的产品的许可证方可使用本软件。标明为升级版本的软件替换和/或补充（也可能使无能）使您有资格使用升级版本的基础的产品，您只可根据本《协议》的条款使用所产生的升级产品。如本软件是您获得许可作为单一产品使用的一套软件程序包中一个组件的升级版本，则本软件只可作为该单一产品包的一部分而使用和转让，并且不可将其分开使用在一台以上的计算机上。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4．著作权。本软件（包括但不限于本软件中所含的任何图象、照片、动画、录像、录音、音乐、文字和附加程序）、随附的印刷材料、及本软件的任何副本的产权和著作权，均由Sakitami拥有。通过使用本软件可访问的内容的一切所有权和知识产权均属于各自内容所有者拥有，并可能受适用著作权或其它知识产权法和条约的保护。   </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本《协议》不授予您使用这些内容的权利。如果这份软件包括只以电子形式提供的文档，您可以打印一份该电子文档。您不可复制本软件随附的印刷材料。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.备份副本。在按照本《协议》安装一份本软件副本后，您可以保留   </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sakitami用以提供给您本软件的原媒体，仅用于备份或存档之用。如果需要原媒体方可在计算机上使用该软件，您可以复制一份该软件副本仅用于备份或存档之用。除本《协议》中明文规定外，您不可复制本软件或随附本软件的印刷材料。  </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">如您是在中华人民共和国取得此软件，下列有限保证适用于您： <span style=\" font-family:\'宋体\'; font-size:12pt;\">网上抄的。。。没有实际意义</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "关于"))
        self.label.setText(_translate("MainWindow", "|匿名信DEMO-v0.0.2|请使用MarkDown语法书写信件|"))
