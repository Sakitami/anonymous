# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
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
        self.label_6.setText(_translate("MainWindow", "匿名名片:"))
        self.label_7.setText(_translate("MainWindow", "未登录"))
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
        self.label_12.setText(_translate("MainWindow", "To:"))
        self.label_13.setText(_translate("MainWindow", "By:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1天"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3天"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10天"))
        self.comboBox.setItemText(3, _translate("MainWindow", "1月"))
        self.comboBox.setItemText(4, _translate("MainWindow", "不清除"))
        self.pushButton_3.setText(_translate("MainWindow", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "发送信件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "关于"))
        self.label.setText(_translate("MainWindow", "|匿名信v0.0.1|请使用MarkDown语法书写信件|"))
