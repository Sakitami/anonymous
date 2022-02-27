import pickle
import pandas as pd
import os
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
        return self.__a


    def delletter(self,index:int):
        self.delindex = index
        self.__delfile = pd.read_csv(self.catalog+"\\data\\letters.csv")
        selfl__deldate = str(self.__delfile.head(self.delindex).values.tolist()[self.delindex-1][3])
        controller2 = Mysql()
        controller2.setinvisible(selfl__deldate)

    def delletter2(self,index:int):
        self.delindex2 = index
        self.__delfile2 = pd.read_csv(self.catalog+"\\data\\send.csv")
        selfl__deldate2 = str(self.__delfile2.head(self.delindex2).values.tolist()[self.delindex2-1][3])
        controller3 = Mysql()
        controller3.setinvisible(selfl__deldate2)
        
    def readletter(self,index:int):
        self.__readmsg = pd.read_csv(self.catalog+"\\data\\letters.csv")

        
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

        self.__msgs = open(self.catalog+"\\data\\letter.html","w")
        self.__msgs.write("<link href=\""+self.catalog+"\\css\\default.css\" rel=\"stylesheet\">")
        self.__msgs.write(self.__readsendmsg.head(index).values.tolist()[index-1][5])
        self.__msgs.close()
        print(self.catalog+b"\data\letter.html")
        webbrowser.open_new_tab(self.catalog+b"\data\letter.html")

if __name__ == '__main__':
    pass