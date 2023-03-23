import database
from model.Client import Client



def crateClientService(Client):
    try:
        query=f"INSERT INTO `qa`.`ip` (`ip`,  `post`) VALUES ('{Client.ip}', '1');"
        database.databaseHandler.execute(query)
        return True
    except:
        return False
    
def updateClientService(Client):
    try:
        query=f"update `qa`.`ip` set `post`=`post`+1 where `ip` = '{Client.ip}';"
        database.databaseHandler.execute(query)
        return True
    except:
        return False
        
def addClientService(Client):
    try:
        try:
            updateClientService(Client)
        except:
            crateClientService(Client)
        return True
    except:
        return False
    

def getClientService(ip):
    try:
        query=f"SELECT `post` FROM  `qa`.`ip` where `ip`= '{ip}';"
        return databaseHandler.show(query)[0][0]
    except:
        return 0
    
def checkClientService(ip):
    if (getClientService(ip)<10):
        return addClientService(Client(ip))
    else:
        return False
