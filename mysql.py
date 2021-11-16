import pandas as pd
from sqlalchemy import create_engine
import os
import pickle

class Mysql():
    def __init__(self):
        ## 初始化命令列表
        self.command = ['select * from letter;','select * from user','insert into letter values (21103310,1)']
        ## 连接Mysql数据库
        self.engine = create_engine('mysql+pymysql://client:02e0be72e034672d2ba5c5b029b7ff2d12345678@45.32.84.140:3306/anonymous')


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
            os.remove('anonymous\\bin\\user.pkl')
        except:
            pass
        finally:
            self.userlistfile = open('anonymous\\bin\\user.pkl','w')
            self.userlistfile.close()
            with open('anonymous\\bin\\user.pkl','wb') as f:
                pickle.dump(self.readuser,f)
        return 1
    
    ## 读取信件
    def readmessage(self,id:str):
        ## 接收用户id
        self.userid = id
        print(self.userid)
        self.readcommand = f"SELECT * FROM letter WHERE receiver = {self.userid}"
        print(self.readcommand)
        ## 执行SQL查询语句,并返回csv文件
        try:
            os.remove('anonymous\\data\\letters.csv')
        except:
            pass
        #try:
        self.letterfile = open('anonymous\\data\\letters.csv','w')
        self.letterfile.close()
        self.readletter = pd.read_sql_query(self.readcommand,self.engine).to_csv('userinterface\\data\\letters.csv',sep=',',index=False,header=['id','sender','receiver','date_send','data_received','del_time','text'])
        self.letterfile = pd.read_csv('anonymous\\data\\letters.csv')
        self.letterfile.drop(['id'],axis=1)
        self.letterfile.to_csv('anonymous\\data\\letters.csv')
        #except:
        #    print("网络连接失败！")
        #    return 0
        ## 将信件保存到本地
        return 1

    def sendmessage(self,messages:str):
        self.sendmes = messages

if __name__ == '__main__':
    test = Mysql()
    test.readmessage(str(21103307))
    #test.readuserlist()
    #test.sendmessage('Hello World!')
    #print(test.readmessage()[0][2])
    #for i in test.readmessage():
    #    list.append(i)
    #print(list)
    #print(type(test.readmessage()))
    #print(str(test.readmessage()))
    #test.readmessage()S