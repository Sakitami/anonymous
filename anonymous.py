import sys
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QThread,pyqtBoundSignal
from window import Ui_MainWindow
from mysql import Mysql
import hashlib

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.letterlist=QStandardItemModel(10,4)
        self.letterlist.setHorizontalHeaderLabels(['发件人','是否已读','发件时间','清除时间'])
        self.tableView_3.setModel(self.letterlist)

        ## 点击登录
        self.pushButton_9.clicked.connect(self.Login)
    

    ## 启动登录线程
    def Login(self):
        ## 将登录按钮设置为禁用,以免多次点击
        self.pushButton_9.setDisabled(True)
        self.pushButton_9.setText("登录中...")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.Login_QThread = LoginThread()
        self.Login_QThread.start()

class LoginThread(QThread):
    ## 登录线程信号
    trigger = pyqtBoundSignal(str)
    def __init__(self):
        super(LoginThread,self).__init__()
    def run(self):

        md5.update(str(myWin.lineEdit_3.text()).encode('utf-8'))
        password = md5.hexdigest()
        userid = (str(myWin.lineEdit_5.text()))
        login_result = controller.userlogin(userid,password.upper())
        if login_result == 1:
            myWin.pushButton_9.setText("登录成功")
            myWin.label_3.setText(userid)
            myWin.label_5.setText("在线")
            pass
        elif login_result == 0:
            myWin.pushButton_9.setEnabled(True)
            myWin.pushButton_9.setText("网络错误")
            myWin.lineEdit_5.setEnabled(True)
            myWin.lineEdit_3.setEnabled(True)
        elif login_result == 2:
            myWin.pushButton_9.setEnabled(True)
            myWin.pushButton_9.setText("登录失败")
            myWin.lineEdit_5.setEnabled(True)
            myWin.lineEdit_3.setEnabled(True)

        print(password+' '+userid)
        pass
if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    md5 = hashlib.md5()
    controller = Mysql()
    app = QApplication(sys.argv)
    myWin = MyMainForm()  ## 初始化
    myWin.setWindowTitle('匿名信')
    myWin.show()          ## 将窗口显示在屏幕
    sys.exit(app.exec_()) ## 确保完整退出