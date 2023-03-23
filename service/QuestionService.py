import database
from model.Question import Question

databaseHandler = database.DataBase()

def getQuestion():
    try:
        api=[]
        query='SELECT * FROM QA.Question;'
        for item in databaseHandler.show(query):
            temp=Question(id=item[0],content=item[1],email=item[2])
            api.append(temp.toApi())
        return {"question": api}
    except:
        return 'ERROR'
    
def addQuestion(question,email):
    try:
        query=f"INSERT INTO `QA`.`Question` (`content`, `email`) VALUES ('{question}', '{email}');"
        databaseHandler.execute(query)
        return True
    except:
        return False
