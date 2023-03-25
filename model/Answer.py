from database import checkResponse


class Answer:
    # 建構式
    # def __init__(self):

    def __init__(self, id='0', answer='',time=''):
        self.id = id
        self. answer =  str(answer)
        self. time =  time
    # 方法(Method)

    def toApi(self):
        self.api={'id': self.id, 'answer': self.answer,'time': self.time}
        return self.api
    def fromApi(self,api):
        print(api)
        try:
            self.id=api['id'] 
        except:
            self.id=0 
        try:
            self.answer= api['answer'] 
        except:
            self.answer=''
        try:
            self.time= api['time'] 
        except:
            self.time=''         
        return True
    def check(self):
        if(checkResponse(self.id) and checkResponse(self.answer)):
            return True
        return False