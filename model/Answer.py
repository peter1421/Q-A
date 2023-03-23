class Answer:
    # 建構式
    # def __init__(self):

    def __init__(self, id='0', answer=''):
        self.id = id
        self. answer =  answer
    # 方法(Method)

    def toApi(self):
        self.api={'id': self.id, 'answer': self.answer}
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
        return True