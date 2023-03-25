import database
from model.Question import Question

def getQuestionService(databaseHandler):
    try:
        api=[]
        query='SELECT * FROM qa.question;'
        for item in databaseHandler.show(query):
            temp=Question(id=item[0],content=item[1],email=item[2])
            api.append(temp.toApi())
        return {"question": api}
    except Exception as e: 
        return {"error":str(e)}
    
def addQuestionService(databaseHandler,question,email):
    try:
        query=f"INSERT INTO `qa`.`question` (`content`, `email`) VALUES ('{question}', '{email}');"
        databaseHandler.execute(query)
        return True
    except:
        return False
