import database
from model.Answer import Answer

def getAnswerService(databaseHandler,id):
    try:
        api=[]
        query=f"""
                select `qa`.`answer`.`answer`,`qa`.`answer`.`time`
                from `qa`.`answer` inner Join `qa`.`question` on `qa`.`question`.`id` =`qa`.`answer`.`id`
                where `qa`.`question`.`id`={id} """
        for item in databaseHandler.show(query):
            temp=Answer(id=id,answer=item[0],time=item[1])
            api.append(temp.toApi())
        return {"answer": api}
    except Exception as e: 
        return {"error":str(e)}

def addAnswerService(databaseHandler,Answer):
    try:
        query=f"INSERT INTO `qa`.`answer` (`id`, `answer`) VALUES ('{Answer.id}', '{Answer.answer}');"
        databaseHandler.execute(query)
        return True
    except:
        return False
