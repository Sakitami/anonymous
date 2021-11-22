import pickle
import pandas as pd
import os
#import markdown
import webbrowser
from mysql import Mysql


class Users():
    def __init__(self):
        self.catalog = os.getcwd()
        self.command = []

    def userlist(self):
        self.__f = open(self.catalog+"\\bin\\user.pkl","rb")
        self.__a = pickle.load(self.__f)
        self.__f.close()
        print(self.__a)
        return self.__a


    def delletter(self,index:int):
        self.delindex = index
        self.__delfile = pd.read_csv(self.catalog+"\\data\\letters.csv")
        selfl__deldate = str(self.__delfile.head(self.delindex).values.tolist()[self.delindex-1][3])
        print(selfl__deldate)
        controller2 = Mysql()
        controller2.setinvisible(selfl__deldate)

    def delletter2(self,index:int):
        self.delindex2 = index
        self.__delfile2 = pd.read_csv(self.catalog+"\\data\\send.csv")
        selfl__deldate2 = str(self.__delfile2.head(self.delindex2).values.tolist()[self.delindex2-1][3])
        print(selfl__deldate2)
        controller3 = Mysql()
        controller3.setinvisible(selfl__deldate2)
        
    def readletter(self,index:int):
        self.__readmsg = pd.read_csv(self.catalog+"\\data\\letters.csv")
        print('1')

        self.__msg = open(self.catalog+"\\data\\letter.html","w")
        self.__msg.write("<link href=\""+self.catalog+"\\css\\default.css\" rel=\"stylesheet\">")
        self.__msg.write(self.__readmsg.head(index).values.tolist()[index-1][5])
        self.__msg.close()
        webbrowser.open_new_tab(self.catalog+"\\data\\letter.html")
        if self.__readmsg.head(index).values.tolist()[index-1][2] == 0:
            controller = Mysql()
            controller.signread(str(self.__readmsg.head(index).values.tolist()[index-1][3]))
        pass

    def readsendletter(self,index:int):
        self.__readsendmsg = pd.read_csv(self.catalog+"\\data\\send.csv")
        print('1')

        self.__msgs = open(self.catalog+"\\data\\letter.html","w")
        self.__msgs.write("<link href=\""+self.catalog+"\\css\\default.css\" rel=\"stylesheet\">")
        self.__msgs.write(self.__readsendmsg.head(index).values.tolist()[index-1][5])
        self.__msgs.close()
        webbrowser.open_new_tab(self.catalog+"\\data\\letter.html")
#    def sendmsg(self):
#        self.__fl = open(self.catalog+"\\bin\\message.pkl","rb")
#        self.__b = pickle.load(self.__fl)
#        self.__fl.close()
#        return self.__b

if __name__ == '__main__':
    #users = Users()
    #users.readletter(1)
    #users.userlist()
    #users.readletter(10)
    pass