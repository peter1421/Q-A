import database
from model.Question import Question

def getQuestionService():
    try:
        api=[]
        query='SELECT * FROM qa.question;'
        for item in database.databaseHandler.show(query):
            temp=Question(id=item[0],content=item[1],email=item[2])
            api.append(temp.toApi())
        return {"question": api}
    except:
        return 'ERROR'
    
def addQuestionService(question,email):
    try:
        query=f"INSERT INTO `qA`.`question` (`content`, `email`) VALUES ('{question}', '{email}');"
        database.databaseHandler.execute(query)
        return True
    except:
        return False
