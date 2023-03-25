import pymysql
import configparser



class DataBase():
    def __init__(self):
        
        self.db = pymysql.connect(
            host=dbhost, user=dbuser, password=dbpass)
        self.cur = self.db.cursor()
        print("連線成功")

    def show(self, query):
        try:
            print(query)
            self.cur.execute(query)
            results = self.cur.fetchall()
            self.db.commit()
            return results
        except:
            self.db.rollback()

    def execute(self, query):
        try:
            print(query)
            self.cur.execute(query)
            self.db.commit()
            print("execute成功")
        except:
            self.db.rollback()

try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    dbhost = config.get('DataBase', 'host')
    dbuser = config.get('DataBase', 'user')
    dbpass = config.get('DataBase', 'pass')
except:
    # dbhost = 'qa-web.c6vvbl5ahndg.us-east-2.rds.amazonaws.com'
    dbhost = '34.80.238.171'
    dbuser='root'
    dbpass='fil12385ki'
    

def checkResponse(api):
    attacker =['#','*',')','root','admin','=','or','//', '--' , '/**/', '#', '--+', '-- -', ';%00']
    if(len(api)>=1 and len(api)<=100):
        for item in attacker:
            for apiWord in api:
                if(item in apiWord):
                    return False
        return True
    return False

