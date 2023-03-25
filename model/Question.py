from database import checkResponse


class Question:
    # 建構式
    # def __init__(self):

    def __init__(self, id='0', content='',email='null@mail'):
        self.id = id
        self. content =  content
        self. email =  email
        self.api=''
    # 方法(Method)

    def toApi(self):
        self.api={'id': self.id, 'content': self.content,'email':self.email}
        return self.api
    def fromApi(self,api):
        print(api)
        try:
            self.id=api['id'] 
        except:
            self.id=0 
        try:
            self.content=api['content'] 
        except:
            self.content='' 
        try:
            self.email= api['mail'] 
        except:
            self.email='' 
        return True
    def check(self):
        if(checkResponse(self.id) and checkResponse(self.content)and checkResponse(self.email)):
            return True
        return False