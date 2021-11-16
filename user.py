import pickle
import os



class Users():
    def __init__(self):
        self.catalog = os.getcwd()
        self.command = []

    ## 处理用户列表，返回给主文件
    def userlist(self):
        self.__f = open(self.catalog+"\\bin\\user.pkl","rb")
        self.a = pickle.load(self.__f)
        self.__f.close()
        print(self.a)
        return self.a

if __name__ == '__main__':
    users = Users()
    users.userlist()