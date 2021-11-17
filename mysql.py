import pandas as pd
from sqlalchemy import create_engine
import os
import pickle
import datetime

class Mysql():
    def __init__(self):
        ## 获取当前文件目录
        self.catalog = os.getcwd()
        ## 初始化命令列表
        self.command = ['select * from letter;','select * from user','insert into letter values (21103310,1)']
        ## 连接Mysql数据库
        self.engine = create_engine('mysql+pymysql://client:02e0be72e034672d2ba5c5b029b7ff2d12345678@45.32.84.140:3306/anonymous')


    ## 设置离线
    def offline(self,id:str):
        self.off_id = id
        try:
            self.off_do = pd.read_sql_query(f'UPDATE user SET status = 0 WHERE id = \'{self.id}\'',self.engine)
        except:
            pass
        return 0

    ## 获取匿名名片信息
    def gainany(self,id:str):
        self.any_id = id
        self.usercheck = pd.read_sql_query(f'SELECT * FROM user WHERE id = \'{str(self.any_id)}\'',self.engine).values.tolist()
        self.any_list = []
        for i in self.usercheck:
            self.any_list.append(i[3])
            self.any_list.append(i[4])
            self.any_list.append(i[5])
            self.any_list.append(i[6])
        return self.any_list

    ## 用户登录
    def userlogin(self,id:str,password:str):
        self.id=id
        self.password=password
        self.logincommand = f'UPDATE user SET status = 1 WHERE id = \'{self.id}\''
        try:
            self.usercheck = pd.read_sql_query(f'SELECT * FROM user WHERE id = \'{self.id}\'',self.engine).values.tolist()
        except:
            print("登陆失败,无网络连接")
            return 0
        try:
            self.usercheck[0][1]
        except:
            print('登陆失败!请检查用户名或密码是否错误')
            return 2
        #print(self.usercheck[0][1])
        if self.usercheck[0][1] != self.password:
            print("登录失败!请检查用户名或密码是否错误")
            return 2
        try: ## TODO 待解决的登录致命错误
            self.loginuser = pd.read_sql_query(self.logincommand,self.engine)
        except:
            print('登陆成功!')
            return 1
        print("登陆成功!")
        return 1

    ## 用户注册
    def useregister(self,id:str,password:str):
        self.id=id
        self.password=password
        try:
            self.checkid = pd.read_sql_query(f"SELECT * from user WHERE id = '{str(self.id)}'",self.engine).values.tolist()
            print(self.checkid)
            #return 0
        except:
            print("网络错误")
            return 0
        if self.checkid != []:
            print("已被占用的id")
            return 2
        try:
            self.doregister = pd.read_sql_query(f"INSERT INTO `user` (`id`, `password`, `status`, `nick1`, `nick2`, `nick3`, `nick_enable`) VALUES ('{str(self.id)}', '{str(self.password)}', '0', '', '', '', '');",self.engine)
        except:
            print("注册成功")
            return 1
    ## 读取用户列表
    def readuserlist(self):
        ## 执行SQL查询语句,并返回列表
        try:
            self.readuser = pd.read_sql_query(self.command[1],self.engine).values.tolist()
        except:
            print("网络连接失败！")
            return 0
        ## 将用户列表保存到本地
        try:
            os.remove(self.catalog+'\\bin\\user.pkl')
        except:
            pass
        finally:
            self.userlistfile = open(self.catalog+'\\bin\\user.pkl','w')
            self.userlistfile.close()
            with open(self.catalog+'\\bin\\user.pkl','wb') as f:
                pickle.dump(self.readuser,f)
        return 1

    ## 读取信件
    def readmessage(self,id:str):
        ## 接收用户id
        self.userid = id
        print(self.userid)
        self.readcommand = f"SELECT * FROM letter WHERE receiver = '{self.userid}'"
        print(self.readcommand)
        ## 执行SQL查询语句,并返回csv文件
        try:
            os.remove(self.catalog+'\\data\\letters.csv')
        except:
            pass
        #try:
        #self.letterfile = open(self.catalog+'\\data\\letters.csv','w')
        #self.letterfile.close()
        try:
            self.readletter = pd.read_sql_query(self.readcommand,self.engine)
            self.readletter = self.readletter[['sender','status','date_send','del_time','text']]
        except:
            print("网络错误")
            return 0 ## 网络错误则返回0
        self.readletter.to_csv(self.catalog+'\\data\\letters.csv')
        print(self.readletter.values.tolist())
        if self.readletter.values.tolist() == []:
            print("没有信件")
            return 2 ## 没有信件则返回2
        ## 将信件保存到本地, 将信件信息列表返回给主文件
        return self.readletter.values.tolist()

    ## 发送信件
    def sendmessage(self,user:str,nick:str,receiver:str,message:str):
        self.senduser = user
        self.sendnick = nick
        self.sendreceive = receiver
        self.sendmsg = message
        try:
            self.usercheck = pd.read_sql_query(f'SELECT * FROM user WHERE id = \'{self.sendreceive}\'',self.engine).values.tolist()
        except:
            print("无网络连接")
            return 0
        try:
            self.usercheck[0][1]
        except:
            print('无该用户')
            return 2
        #try:
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(self.senduser+'|'+self.sendnick+'|'+self.sendreceive+'|'+self.sendmsg)
        self.doregister = pd.read_sql_query(f"INSERT INTO `letter` (`id`, `sender`, `receiver`, `status`, `date_send`, `del_time`, `text`) VALUES ('{str(self.senduser)}', '{str(self.sendnick)}', '{str(self.sendreceive)}', '', '{dt}', '', {self.sendmsg});",self.engine)
        #    print("发送成功")
        #    return 1 ## 返回发送成功结果
        #except:
        #    print("发送成功")
        #    return 1
        #    return 0 ## 返回错误类型        
        #pass

if __name__ == '__main__':
    #test = Mysql()
    #test.readmessage(str('Sakitami'))
    #test.sendmessage('hanyi2','BlackCat','Sakitami','woshidashabi')
    #test.readuserlist()
    #test.useregister('wrewr','4DA6EDB16DAD7148938AC3463EDACD62')
    #test.sendmessage('Hello World!')
    #print(test.readmessage()[0][2])
    #for i in test.readmessage():
    #    list.append(i)
    #print(list)
    #print(type(test.readmessage()))
    #print(str(test.readmessage()))
    #test.readmessage()
    pass