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
        return {"qestion": api}
    except:
        return 'ERROR'
    
def addQuestion(question,email):
    try:
        query=f"INSERT INTO `QA`.`Question` (`content`, `mail`) VALUES ('{question}', '{email}');"
        databaseHandler.execute(query)
        return True
    except:
        return False

