import pickle
import os



class Users():
    def __init__(self):
        self.catalog = os.getcwd()
        self.command = []

    ## �����û��б������ظ����ļ�
    def userlist(self):
        self.__f = open(self.catalog+"\\bin\\user.pkl","rb")
        self.__a = pickle.load(self.__f)
        self.__f.close()
        print(self.__a)
        return self.__a

#    def sendmsg(self):
#        self.__fl = open(self.catalog+"\\bin\\message.pkl","rb")
#        self.__b = pickle.load(self.__fl)
#        self.__fl.close()
#        return self.__b

if __name__ == '__main__':
    users = Users()
    users.userlist()