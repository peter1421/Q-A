import pymysql
import os
import configparser



class DataBase():
    def __init__(self):
        
        self.db = pymysql.connect(
            host=dbhost, user=dbuser, password=dbpass)
        self.cur = self.db.cursor()
        print("連線成功")

    def show(self, query):
        try:
            self.cur.execute(query)
            results = self.cur.fetchall()
            self.db.commit()
            return results
        except:
            self.db.rollback()

    def execute(self, query):
        try:
            self.cur.execute(query)
            self.db.commit()
            print("execute成功")
        except:
            self.db.rollback()

# t = DataBase()
config = configparser.ConfigParser()
config.read('config.ini')
dbhost = config.get('DataBase', 'host')
dbuser = config.get('DataBase', 'user')
dbpass = config.get('DataBase', 'pass')