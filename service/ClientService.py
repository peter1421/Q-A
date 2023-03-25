import database
from model.Client import Client



def crateClientService(databaseHandler,Client):
    try:
        query=f"INSERT INTO `qa`.`ip` (`ip`,  `post`) VALUES ('{Client.ip}', '1');"
        databaseHandler.execute(query)
        return True
    except:
        return False
    
def updateClientService(databaseHandler,Client):
    try:
        query=f"update `qa`.`ip` set `post`=`post`+1 where `ip` = '{Client.ip}';"
        databaseHandler.execute(query)
        return True
    except:
        return False
        
def addClientService(databaseHandler,Client):
    try:
        try:
            updateClientService(databaseHandler,Client)
        except:
            crateClientService(databaseHandler,Client)
        return True
    except:
        return False
    

def getClientService(databaseHandler,ip):
    try:
        query=f"SELECT `post` FROM  `qa`.`ip` where `ip`= '{ip}';"
        return databaseHandler.show(query)[0][0]
    except:
        return 0
    
def checkClientService(databaseHandler,ip):
    if (getClientService(databaseHandler,ip)<100):
        return addClientService(databaseHandler,Client(ip))
    else:
        print('已超過次數')
        return False

