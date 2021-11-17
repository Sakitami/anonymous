import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread,pyqtBoundSignal
from window import Ui_MainWindow
from mysql import Mysql
from user import Users
import time
import hashlib

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        #self.letterlist=QStandardItemModel(10,4)
        #self.letterlist.setHorizontalHeaderLabels(['发件人','是否已读','发件时间','清除时间'])
        #self.tableView_3.setModel(self.letterlist)


        # 该部分为前后端连接
        ## 点击登录按钮
        self.pushButton_9.clicked.connect(self.Login)
        ## 点击注册按钮
        self.pushButton_10.clicked.connect(self.Register)
        ## 点击添加/删除按钮
        self.pushButton.clicked.connect(self.EditAny)
        ## 点击手动刷新按钮 -- 获取信件
        self.pushButton_2.clicked.connect(self.ReadMessage)
        ## 点击发送按钮-- 发送信件
        self.pushButton_3.clicked.connect(self.PushMessage)


    ## 启动修改匿名线程
    def EditAny(self):
        self.pushButton.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.EditAny_QThread = EditanyThread()
        self.EditAny_QThread.start()

    ## 启动登录线程
    def Login(self):
        ## 将登录按钮设置为禁用,以免多次点击
        self.pushButton_9.setDisabled(True)
        self.pushButton_9.setText("登录中...")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.Login_QThread = LoginThread()
        self.Login_QThread.start()

    ## 启动获取用户列表线程
    def Userlist(self):
        self.Userlist_QThread = UserlistThread()
        self.Userlist_QThread.start()
        self.Userlist_QThread.wait()

    ## 启动注册线程
    def Register(self):
        self.pushButton_10.setDisabled(True)
        self.pushButton_10.setText("正在注册...")
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.Register_QThread = RegisterThread()
        self.Register_QThread.start()

    ## 启动获取信件线程
    def ReadMessage(self):
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.setText("刷新中")
        self.ReadMessage_QThread = ReadMessageThread()
        self.ReadMessage_QThread.start()
        #self.ReadMessage_QThread.stop()
        pass

    ## 启动发送信件线程
    def PushMessage(self):
        self.lineEdit_6.setDisabled(True)
        self.comboBox_2.setDisabled(True)
        self.textEdit_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.PushMessage_QThread = PushMessageThread()
        self.PushMessage_QThread.start()
        self.PushMessage_QThread.wait()
        pass

## 发送信件线程逻辑实现
class PushMessageThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(PushMessageThread,self).__init__()
    def run(self):
        strtest = (repr(myWin.textEdit_2.toPlainText()))
        print(myWin.lineEdit_6.text())
        if myWin.textEdit_2.toPlainText() == '' or myWin.lineEdit_6.text() == '':
            print('信件不能为空')
        else:
            push_check =  controller.sendmessage(str(myWin.lineEdit_5.text()),myWin.comboBox_2.currentText(),myWin.lineEdit_6.text(),strtest)
            myWin.pushButton_3.setEnabled(True)
            myWin.lineEdit_6.setEnabled(True)
            myWin.comboBox_2.setEnabled(True)
            myWin.textEdit_2.setEnabled(True)
            if push_check == 1:
                myWin.pushButton_3.setText("发送成功")

            else:
                myWin.pushButton_3.setText("发送失败")
        print(strtest)
        pass ## TODO 发送信件功能

## 获取信件线程逻辑实现
class ReadMessageThread(QThread):  ## FIXME 线程冲突问题
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(ReadMessageThread,self).__init__()
        self.readmsguserid = str(myWin.lineEdit_5.text())
        self.module = QtGui.QStandardItemModel()
        self.module.setHorizontalHeaderLabels(['发件人','是否已读','发件时间','清除时间'])
    def run(self):
        self.readmsglist = controller.readmessage(self.readmsguserid)
        if self.readmsglist == 0:
            pass
        elif self.readmsglist == 2:
            pass
        else:
            print(len(self.readmsglist[0]))
            for i in range(0,len(self.readmsglist)):
                for j in range(0,len(self.readmsglist[i])-1):
                    self.module.setItem(i,j,QtGui.QStandardItem(str(self.readmsglist[i][j])))
        #for i in range(0,len(self.readmsguserid)):
        #    for j in range(0,4):
        #        self.module.setItem(i,j,QtGui.QStandardItem(str(self.readmsglist[i][j])))
            myWin.tableView_3.setModel(self.module)
            myWin.pushButton_2.setEnabled(True)
            myWin.pushButton_2.setText("手动刷新")

        pass ## TODO 获取信件线程逻辑实现

## 匿名名片显示线程逻辑实现
class AnonymousShowThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        self.showanyuserid = (str(myWin.lineEdit_5.text()))
        super(AnonymousShowThread,self).__init__()
    def run(self):
        self.anylist = controller.gainany(self.showanyuserid)
        myWin.label_7.setText(self.anylist.pop())
        print(self.anylist)
        myWin.listWidget_2.addItems(self.anylist)
        myWin.comboBox_2.clear()
        myWin.comboBox_2.addItems(self.anylist)
        pass

## 修改匿名线程逻辑实现
class EditanyThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(EditanyThread,self).__init__()
    def run(self):
        pass ## TODO 修改匿名功能

## 同步线程
class SyncThread(QThread):
    ## 线程信号
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(SyncThread,self).__init__()
        self.sync_user = (str(myWin.lineEdit_5.text()))
    def run(self):
        while True:
            time.sleep(60)
            myWin.Userlist()
            #myWin.ReadMessage()
            #controller.readmessage(id=self.sync_user)
            print('被执行')

## 注册线程逻辑实现
class RegisterThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(RegisterThread,self).__init__()
        self.username = str(myWin.lineEdit_7.text())
        self.password = str(myWin.lineEdit_4.text()).encode('utf-8')
        self.verify = str(myWin.lineEdit_8.text()).encode('utf-8')
    def run(self):
        ## 判断用户两次输入密码是否相等
        if  self.username == '' or str(myWin.lineEdit_4) == '' or str(myWin.lineEdit_8) =='':
            myWin.pushButton_10.setEnabled(True)
            myWin.pushButton_10.setText("非法输入")
            myWin.lineEdit_4.setEnabled(True)
            myWin.lineEdit_7.setEnabled(True)
            myWin.lineEdit_8.setEnabled(True)
            pass
            #return 0
        elif  self.password != self.verify:
            myWin.pushButton_10.setEnabled(True)
            myWin.pushButton_10.setText("密码有误")
            myWin.lineEdit_4.setEnabled(True)
            myWin.lineEdit_7.setEnabled(True)
            myWin.lineEdit_8.setEnabled(True)
            #return 0
        else:
            md5_2.update(self.password)
            finalpassword = md5_2.hexdigest()
            checkresult = controller.useregister(self.username,finalpassword.upper())
            if checkresult == 1:
                myWin.pushButton_10.setEnabled(True)
                myWin.pushButton_10.setText("注册成功")
                myWin.lineEdit_4.setEnabled(True)
                myWin.lineEdit_7.setEnabled(True)
                myWin.lineEdit_8.setEnabled(True)
            elif checkresult == 2:
                myWin.pushButton_10.setEnabled(True)
                myWin.pushButton_10.setText("ID被占用")
                myWin.lineEdit_4.setEnabled(True)
                myWin.lineEdit_7.setEnabled(True)
                myWin.lineEdit_8.setEnabled(True)
            elif checkresult == 0:
                myWin.pushButton_10.setEnabled(True)
                myWin.pushButton_10.setText("网络错误")
                myWin.lineEdit_4.setEnabled(True)
                myWin.lineEdit_7.setEnabled(True)
                myWin.lineEdit_8.setEnabled(True)
                #return 0
        pass

## 登录线程逻辑实现
class LoginThread(QThread):
    ## 登录线程信号
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(LoginThread,self).__init__()
    def run(self):

        ## 对密码进行加密
        md5.update(str(myWin.lineEdit_3.text()).encode('utf-8'))
        password_login = md5.hexdigest()
        userid = (str(myWin.lineEdit_5.text()))
        ## 调用controller的userlogin方法实现登录
        login_result = controller.userlogin(userid,password_login.upper())
        if login_result == 1:  ## 成功登录，设置状态为在线
            myWin.pushButton_9.setText("登录成功")
            myWin.label_3.setText(userid)
            myWin.label_5.setText("在线")
            myWin.Userlist()
            myWin.pushButton.setEnabled(True)
            myWin.tableView_3.setEnabled(True)
            myWin.pushButton_2.setEnabled(True)
            myWin.lineEdit_6.setEnabled(True)
            myWin.comboBox_2.setEnabled(True)
            myWin.pushButton_3.setEnabled(True)
            myWin.textEdit_2.setEnabled(True)
            myWin.lineEdit.setEnabled(True)
            ceshishow = AnonymousShowThread()
            ceshishow.start()
            self.Sync_QThread = SyncThread()
            self.Sync_QThread.start()
        elif login_result == 0:  ## 网络错误
            myWin.pushButton_9.setEnabled(True)
            myWin.pushButton_9.setText("网络错误")
            myWin.lineEdit_5.setEnabled(True)
            myWin.lineEdit_3.setEnabled(True)
        elif login_result == 2:  ## 用户名或密码不存在或错误
            myWin.pushButton_9.setEnabled(True)
            myWin.pushButton_9.setText("登录失败")
            myWin.lineEdit_5.setEnabled(True)
            myWin.lineEdit_3.setEnabled(True)

        print(password_login+' '+userid)
        pass

## 用户列表线程逻辑实现
class UserlistThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(UserlistThread,self).__init__()
    def run(self): 
        controller.readuserlist()
        self.orguserlist = user_controller.userlist()
        self.userlist = []
        for i in self.orguserlist:
            if i[2]:
                self.userlist.append(str(i[0])+'|在线')
            else:
                self.userlist.append(str(i[0])+'|离线')
       #for i in self.userlist:
        myWin.listWidget.clear()
        myWin.listWidget.addItems(self.userlist)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    md5 = hashlib.md5()
    md5_2 = hashlib.md5()
    controller = Mysql()
    user_controller = Users()
    app = QApplication(sys.argv)
    myWin = MyMainForm()  ## 初始化
    myWin.setWindowTitle('匿名信')
    myWin.show()          ## 将窗口显示在屏幕

    #sys.exit(app.exec_()) ## 确保完整退出
    app.exec_()
    controller.offline(str(myWin.lineEdit_3.text()))