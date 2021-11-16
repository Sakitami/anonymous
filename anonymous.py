import sys
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, Qt,pyqtBoundSignal
from window import Ui_MainWindow
from mysql import Mysql
from user import Users
import hashlib

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.letterlist=QStandardItemModel(10,4)
        self.letterlist.setHorizontalHeaderLabels(['发件人','是否已读','发件时间','清除时间'])
        self.tableView_3.setModel(self.letterlist)

        ## 点击登录按钮
        self.pushButton_9.clicked.connect(self.Login)
        ## 点击注册按钮
        self.pushButton_10.clicked.connect(self.Register)

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

    ## 启动注册线程
    def Register(self):
        self.pushButton_10.setDisabled(True)
        self.pushButton_10.setText("正在注册...")
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_8.setEnabled(False)
        self.Register_QThread = RegisterThread()
        self.Register_QThread.start()

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
            pass
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

    sys.exit(app.exec_()) ## 确保完整退出