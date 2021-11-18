import pickle
import pandas as pd
import os
#import markdown
import webbrowser



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

    def readletter(self,index:int):
        self.__readmsg = pd.read_csv(self.catalog+"\\data\\letters.csv")
        print('1')
        self.__msg = open(self.catalog+"\\data\\letter.html","w")
        self.__msg.write("<link href=\""+self.catalog+"\\css\\default.css\""+" rel=\"stylesheet\">")
        self.__msg.write(self.__readmsg.head(index).values.tolist()[index-1][5])
        self.__msg.close()
        webbrowser.open_new_tab(self.catalog+"\\data\\letter.html")

        pass

#    def sendmsg(self):
#        self.__fl = open(self.catalog+"\\bin\\message.pkl","rb")
#        self.__b = pickle.load(self.__fl)
#        self.__fl.close()
#        return self.__b

if __name__ == '__main__':
    #users = Users()
    #users.userlist()
    #users.readletter(10)
    pass