import database



def addAnswerService(Answer):
    try:
        query=f"INSERT INTO `QA`.`answer` (`id`, `answer`) VALUES ('{Answer.id}', '{Answer.answer}');"
        database.databaseHandler.execute(query)
        return True
    except:
        return False
