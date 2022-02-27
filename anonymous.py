import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread,pyqtBoundSignal
from window import Ui_MainWindow
from mysql import Mysql
from user import Users
import time
import hashlib
import qtvscodestyle as qtvsc

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

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
        ## 点击信件中某项
        self.tableView_3.clicked.connect(self.EnableViewMsg)

        ## 点击已发信件中某项
        self.tableView_4.clicked.connect(self.EnableSendViewMsg)

        ## 点击查看信件按钮
        self.pushButton_8.clicked.connect(self.ViewMsg)
        ## 点击已发信件查看信件按钮
        self.pushButton_14.clicked.connect(self.ViewSendMsg)
        ## 点击手动刷新(已发信件)按钮
        self.pushButton_4.clicked.connect(self.ReadSendMessage)

        ## 点击双向删除
        self.pushButton_7.clicked.connect(self.DelAllLtr)
        self.pushButton_13.clicked.connect(self.DelAllLtr2)

        #
        #

    ## 自动刷新邮件线程
    def autosyncletter(self,check:int):
        if check == 1:
            self.ReadMessage_QThread.start()
        elif check == 2:
            self.SendMeMessage_QThread.start()

    ## 启动双向删除线程
    def DelAllLtr(self):
        self.pushButton_7.setDisabled(True)
        self.pushButton_7.setText("删除中...")
        self.pushButton_8.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.DelAllLetter_QThread = DelAllLetter()
        #self.DelAllLetter_QThread.trigger.connect(self.autosyncletter)
        self.DelAllLetter_QThread.start()

    def DelAllLtr2(self):
        self.pushButton_13.setDisabled(True)
        self.pushButton_13.setText("删除中")
        self.pushButton_14.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.DelAllLetter2_QThread = DelAllLetter2()
        #self.DelAllLetter2_QThread.trigger.connect(self.autosyncletter)
        self.DelAllLetter2_QThread.start()


    ## 启动查看信件线程
    def ViewMsg(self):
        self.ViewMsg_QThread = ViewMsgMK()
        self.ViewMsg_QThread.start()
    
    def ViewSendMsg(self):
        self.ViewSendMsg_QThread = ViewSendMsgMK()
        self.ViewSendMsg_QThread.start()

    ## 激活阅读信件按钮
    def EnableViewMsg(self):
        self.pushButton_8.setEnabled(True)
    ## 激活阅读信件(已读)按钮
    def EnableSendViewMsg(self):
        self.pushButton_14.setEnabled(True)
    
    ## 启动修改匿名线程
    def EditAny(self):
        self.pushButton.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.EditAny_QThread = EditanyThread()
        self.EditAny_QThread.start()
        self.EditAny_QThread.quit()
        self.EditShow_QThread = AnonymousShowThread()
        self.EditShow_QThread.start()

    ## 启动登录线程
    def Login(self):
        ## 将登录按钮设置为禁用,以免多次点击
        self.groupBox_3.setDisabled(True)
        self.groupBox_4.setDisabled(True)
        self.pushButton_9.setText("登录中...")
        self.Login_QThread = LoginThread()
        self.Login_QThread.start()

    ## 启动获取用户列表线程
    def Userlist(self):
        self.Userlist_QThread = UserlistThread()
        self.Userlist_QThread.start()
        self.Userlist_QThread.wait()

    ## 启动注册线程
    def Register(self):
        self.pushButton_10.setText("正在注册...")
        self.groupBox_3.setDisabled(True)
        self.groupBox_4.setDisabled(True)
        self.Register_QThread = RegisterThread()
        self.Register_QThread.start()

    ## 启动获取已发信件线程
    def ReadSendMessage(self):
        self.pushButton_4.setDisabled(True)
        self.pushButton_4.setText("刷新中")
        self.SendMeMessage_QThread= SendMeMessageThread()
        self.SendMeMessage_QThread.start()

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
        #self.PushMessage_QThread.wait()
        pass

    ## 启动刷新匿名名片显示线程
    def Refreshcard(self):
        self.AnonymousShow_QThread = AnonymousShowThread()
        self.AnonymousShow_QThread.start()


## 双向删除信件线程逻辑实现
class DelAllLetter(QThread):
    trigger = pyqtBoundSignal(int)
    def __init__(self):
        super(DelAllLetter,self).__init__()
        
    def run(self):
        self.index1 = myWin.tableView_3.currentIndex().row()+1
        if self.index1 == 0:
            ## 没有选择
            myWin.pushButton_2.setEnabled(True)
            myWin.pushButton_8.setEnabled(True)
            myWin.pushButton_7.setEnabled(True)
            myWin.pushButton_7.setText("双向删除")
        else:
            user_controller.delletter(self.index1)
            myWin.pushButton_7.setText("请刷新")
            myWin.pushButton_2.setEnabled(True)
        #self.trigger.emit(1)
        pass ## TODO 好想摸鱼
class DelAllLetter2(QThread):
    trigger = pyqtBoundSignal(int)
    def __init__(self):
        super(DelAllLetter2,self).__init__()
        
    def run(self):
        self.index2 = myWin.tableView_4.currentIndex().row()+1
        if self.index2 == 0:
            ## 没有选择
            myWin.pushButton_4.setEnabled(True)
            myWin.pushButton_13.setEnabled(True)
            myWin.pushButton_14.setEnabled(True)
            myWin.pushButton_13.setText("双向删除")
        else:
            user_controller.delletter2(self.index2)
            myWin.pushButton_13.setText("请刷新")
            myWin.pushButton_4.setEnabled(True)
        #self.trigger.emit(2)
        pass ## TODO 好想摸鱼

## 查看已发信件线程逻辑实现
class SendMeMessageThread(QThread):  ## FIXME 线程冲突问题
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(SendMeMessageThread,self).__init__()
        
        self.module2 = QtGui.QStandardItemModel()
        self.module2.setHorizontalHeaderLabels(['收件人','是否已读','发件时间','清除时间'])
    def run(self):
        self.sendmsguserid = str(myWin.lineEdit_5.text())
        self.readsendmsglist = controller.readsendmessage(self.sendmsguserid)
        if self.readsendmsglist == 0:
            myWin.pushButton_4.setText("网络错误")
        elif self.readsendmsglist == 2:
            myWin.pushButton_4.setText("手动刷新")
        else:
            for i in range(0,len(self.readsendmsglist)):
                for j in range(0,len(self.readsendmsglist[i])-1):
                    if self.readsendmsglist[i][j] == 0:
                        self.module2.setItem(i,j,QtGui.QStandardItem("否"))
                    elif self.readsendmsglist[i][j] == 1:
                        self.module2.setItem(i,j,QtGui.QStandardItem("是"))
                    else:
                        self.module2.setItem(i,j,QtGui.QStandardItem(str(self.readsendmsglist[i][j])))
            myWin.pushButton_4.setText("手动刷新")
        #for i in range(0,len(self.readmsguserid)):
        #    for j in range(0,4):
        #        self.module.setItem(i,j,QtGui.QStandardItem(str(self.readmsglist[i][j])))
        myWin.tableView_4.setModel(self.module2)
        myWin.pushButton_4.setEnabled(True)
        myWin.pushButton_13.setEnabled(True)
        myWin.pushButton_14.setEnabled(True)
        myWin.pushButton_13.setText("双向删除")

## 查看信件线程逻辑实现
class ViewMsgMK(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(ViewMsgMK,self).__init__()
    def run(self):
        if int(myWin.tableView_3.currentIndex().row()) != -1 :
            user_controller.readletter(myWin.tableView_3.currentIndex().row()+1)
            pass ## TODO 查看信件

## 查看已发信件线程逻辑实现
class ViewSendMsgMK(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(ViewSendMsgMK,self).__init__()
    def run(self):
        if int(myWin.tableView_4.currentIndex().row()) != -1 :
            user_controller.readsendletter(myWin.tableView_4.currentIndex().row()+1)
            pass ## TODO 查看信件

## 发送信件线程逻辑实现
class PushMessageThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(PushMessageThread,self).__init__()
    def run(self):
        strtest = myWin.textEdit_2.toPlainText()## (repr(myWin.textEdit_2.toPlainText()))
        if myWin.textEdit_2.toPlainText() == '' or myWin.lineEdit_6.text() == '':  ## 信件为空
            myWin.pushButton_3.setText("有空项")
        elif myWin.comboBox_2.currentText() == '':
            myWin.pushButton_3.setText("无匿名值")
        else:
            push_check =  controller.sendmessage(str(myWin.lineEdit_5.text()),myWin.comboBox_2.currentText(),myWin.lineEdit_6.text(),strtest)
            if push_check == 1:
                myWin.pushButton_3.setText("发送成功")
            elif push_check == 2:
                myWin.pushButton_3.setText("无该用户")
            elif push_check == 3:
                myWin.pushButton_3.setText("不能自发")
            else:
                myWin.pushButton_3.setText("发送失败")
        myWin.pushButton_3.setEnabled(True)
        myWin.lineEdit_6.setEnabled(True)
        myWin.comboBox_2.setEnabled(True)
        myWin.textEdit_2.setEnabled(True)
        myWin.pushButton_7.setText("双向删除")

## 获取信件线程逻辑实现
class ReadMessageThread(QThread):  ## FIXME 线程冲突问题
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(ReadMessageThread,self).__init__()
        
        self.module = QtGui.QStandardItemModel()
        self.module.setHorizontalHeaderLabels(['发件人','是否已读','发件时间','清除时间'])
    def run(self):
        self.readmsguserid = str(myWin.lineEdit_5.text())
        self.readmsglist = controller.readmessage(self.readmsguserid)
        if self.readmsglist == 0:
            myWin.pushButton_2.setText("网络错误")
        elif self.readmsglist == 2:
            myWin.pushButton_2.setText("手动刷新")
        else:
            for i in range(0,len(self.readmsglist)):
                for j in range(0,len(self.readmsglist[i])-1):
                    if self.readmsglist[i][j] == 0:
                        self.module.setItem(i,j,QtGui.QStandardItem("否"))
                    elif self.readmsglist[i][j] == 1:
                        self.module.setItem(i,j,QtGui.QStandardItem("是"))
                    else:
                        self.module.setItem(i,j,QtGui.QStandardItem(str(self.readmsglist[i][j])))
            myWin.pushButton_2.setText("手动刷新")
        #for i in range(0,len(self.readmsguserid)):
        #    for j in range(0,4):
        #        self.module.setItem(i,j,QtGui.QStandardItem(str(self.readmsglist[i][j])))
        myWin.tableView_3.setModel(self.module)
        myWin.pushButton_2.setEnabled(True)
        myWin.pushButton_8.setEnabled(True)
        myWin.pushButton_7.setEnabled(True)
        

        pass ## TODO 获取信件线程逻辑实现

## 匿名名片显示线程逻辑实现
class AnonymousShowThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        
        super(AnonymousShowThread,self).__init__()
    def run(self):
        self.showanyuserid = (str(myWin.lineEdit_5.text()))
        time.sleep(5)
        myWin.pushButton_2.setDisabled(True)
        myWin.pushButton.setText("刷新中...")
        self.anylist = controller.gainany(self.showanyuserid)
        if self.anylist == 0:
            myWin.pushButton.setText("网络错误")
        else:
            self.anylist.pop()
            myWin.listWidget_2.addItems(self.anylist)
            myWin.listWidget_2.clear()
            myWin.listWidget_2.addItems(self.anylist)
            myWin.pushButton.setText("添加/删除")
        myWin.lineEdit.setEnabled(True)
        myWin.pushButton.setEnabled(True)
        myWin.pushButton_2.setEnabled(True)
        myWin.pushButton_4.setEnabled(True)
        myWin.pushButton_13.setEnabled(True)

## 修改匿名线程逻辑实现
class EditanyThread(QThread):
    trigger = pyqtBoundSignal(int)
    #trigger.connect()
    def __init__(self):
        super(EditanyThread,self).__init__()
        self.editdanylist = []
    def run(self):
        self.check_result_edit = controller.editany(str(myWin.lineEdit_5.text()),str(myWin.lineEdit.text()))
        if self.check_result_edit == 1:
            myWin.pushButton.setText("删除完成")
        elif self.check_result_edit == 2:
            myWin.pushButton.setText("添加完成")
        elif self.check_result_edit == 3:
            myWin.pushButton.setText("名片已满")
        else:
            myWin.pushButton.setText("修改失败")
        #self.trigger.emit(1)
        myWin.comboBox_2.clear()
        self.editanylist = controller.gainany(str(myWin.lineEdit_5.text()))
        for i in range(0,3):
            if self.editanylist[i] != '':
                self.editdanylist.append(self.editanylist[i])
        myWin.comboBox_2.addItems(self.editdanylist)
        #myWin.lineEdit.setEnabled(True)
        #myWin.pushButton.setEnabled(True)
        pass ## TODO 修改匿名功能

## 同步线程
class SyncThread(QThread):
    ## 线程信号
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(SyncThread,self).__init__()
        
    def run(self):
        self.sync_user = (str(myWin.lineEdit_5.text()))
        while True:
            time.sleep(60)
            myWin.Userlist()
            #myWin.ReadMessage()
            #controller.readmessage(id=self.sync_user)

## 注册线程逻辑实现
class RegisterThread(QThread):
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(RegisterThread,self).__init__()

    def run(self):
        ## 判断用户两次输入密码是否相等        
        self.username = str(myWin.lineEdit_7.text())
        self.password = str(myWin.lineEdit_4.text()).encode('utf-8')
        self.verify = str(myWin.lineEdit_8.text()).encode('utf-8')
        if  self.username == '' or str(myWin.lineEdit_4) == '' or str(myWin.lineEdit_8) =='':
            
            myWin.pushButton_10.setText("非法输入")
            self.quit()
            #return 0
        elif  self.password != self.verify:
            myWin.pushButton_10.setText("密码有误")
            #return 0
        else:
            md5_2.update(self.password)
            finalpassword = md5_2.hexdigest()
            checkresult = controller.useregister(self.username,finalpassword.upper())
            if checkresult == 1:
                myWin.pushButton_10.setText("注册成功")
            elif checkresult == 2:
                myWin.pushButton_10.setText("ID被占用")
            elif checkresult == 0:
                myWin.pushButton_10.setText("网络错误")
                #return 0
        myWin.groupBox_4.setEnabled(True)
        if myWin.lineEdit_5.text()!= '':
            myWin.groupBox_3.setEnabled(True)
        pass

## 登录线程逻辑实现
class LoginThread(QThread):
    ## 登录线程信号
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(LoginThread,self).__init__()
    def run(self):

        ## 对密码进行加密
        global md5
        del md5
        md5 = hashlib.md5()
        md5.update(str(myWin.lineEdit_3.text()).encode('utf-8'))
        password_login = md5.hexdigest()
        userid = (str(myWin.lineEdit_5.text()))
        ## 调用controller的userlogin方法实现登录
        login_result = controller.userlogin(userid,password_login.upper())
        if login_result == 1:  ## 成功登录，设置状态为在线
            myWin.pushButton_9.setText("登录成功")
            myWin.label_3.setText(userid.lower())
            myWin.label_5.setText("在线")
            myWin.Userlist()
            myWin.tableView_3.setEnabled(True)
            myWin.lineEdit_6.setEnabled(True)
            myWin.comboBox_2.setEnabled(True)
            myWin.pushButton_3.setEnabled(True)
            myWin.textEdit_2.setEnabled(True)
            myWin.groupBox_4.setEnabled(True)
            myWin.tableView_4.setEnabled(True)
            myWin.pushButton_14.setEnabled(True)
            ceshishow = AnonymousShowThread()
            ceshishow.start()
            ceshishow.quit()
            self.Sync_QThread = SyncThread()
            self.Sync_QThread.start()
            myWin.comboBox_2.clear()
            myWin.comboBox_2.addItems(controller.gainany(str(myWin.lineEdit_5.text())))
        elif login_result == 0:  ## 网络错误
            myWin.groupBox_3.setEnabled(True)
            myWin.groupBox_4.setEnabled(True)
            myWin.pushButton_9.setText("网络错误")
        elif login_result == 2:  ## 用户名或密码不存在或错误
            myWin.groupBox_3.setEnabled(True)
            myWin.groupBox_4.setEnabled(True)
            myWin.pushButton_9.setText("登录失败")

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
    stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.DARK_VS)
    myWin.setWindowTitle('匿名信')
    myWin.setWindowIcon(QtGui.QIcon('logo.png'))
    myWin.setStyleSheet(stylesheet)
    myWin.show()          ## 将窗口显示在屏幕
    #sys.exit(app.exec_()) ## 确保完整退出
    app.exec_()
    controller.offline(str(myWin.lineEdit_3.text()))