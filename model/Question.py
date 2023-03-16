# # 汽車類別
# class Cars:
#     # 建構式
#     def __init__(self, color, seat):
#         self.color = color  # 顏色屬性
#         self.seat = seat  # 座位屬性
#     # 方法(Method)
#     def drive(self):
#         print(f"My car is {self.color} and has {self.seat} seats.")
# mazda = Cars("blue", 4)
# mazda.drive()  #執行結果：My car is blue and has 4 seats.

# 汽車類別
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
