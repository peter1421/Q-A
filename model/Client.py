from database import  checkResponse


class Client:
    # 建構式
    # def __init__(self):

    def __init__(self, ip, post=0):
        self.ip = ip
        self. post =  post
    # 方法(Method)

    def toApi(self):
        self.api={'ip': self.ip, 'post': self.post}
        return self.api
    def fromApi(self,api):
        print(api)
        try:
            self.id=api['ip'] 
        except:
            self.ip=0 
        try:
            self.post= api['post'] 
        except:
            self.post=''     
        return True
    def check(self):
        if(checkResponse(self.ip)):
            return True
        return False