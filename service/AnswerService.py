import database
from model.Answer import Answer

def getAnswerService(id):
    try:
        api=[]
        query=f"""
                select `qa`.`answer`.`answer`,`qa`.`answer`.`time`
                from `qa`.`answer` inner Join `qa`.`question` on `qa`.`question`.`id` =`qa`.`answer`.`id`
                where `qa`.`question`.`id`={id} """
        for item in database.databaseHandler.show(query):
            print(item)
            temp=Answer(id=id,answer=item[0],time=item[1])
            api.append(temp.toApi())
        return {"answer": api}
    except:
        return 'ERROR'

def addAnswerService(Answer):
    try:
        query=f"INSERT INTO `qA`.`answer` (`id`, `answer`) VALUES ('{Answer.id}', '{Answer.answer}');"
        database.databaseHandler.execute(query)
        return True
    except:
        return False
