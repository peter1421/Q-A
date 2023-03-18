import database
from model.Question import Question

databaseHandler = database.DataBase()

def getQuestion():
    try:
        api=[]
        query='SELECT * FROM QA.Question;'
        for item in databaseHandler.show(query):
            temp=Question(item[0],item[1],item[2],item[3])
            api.append(temp.toApi())
        return api
    except:
        return []