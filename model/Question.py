class Question:
    # 建構式
    # def __init__(self):

    def __init__(self, id, content,mail,answer):
        self.id = id
        self. content =  content
        self. mail =  mail
        self. answer =  answer
        self.api=''
    # 方法(Method)

    def toApi(self):
        self.api={'id': self.id, 'content': self.content,'mail':self.mail,'answer':self.answer}
        return self.api
