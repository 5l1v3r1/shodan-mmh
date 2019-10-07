import redis
from pymongo import MongoClient

# you can create your own serve in this file 

class RedisServe():
    def __init__(self, isHost):
        self.isHost = isHost

    def CheckConnection(self):
        try:
            conn = redis.StrictRedis(
                host=self.isHost,
                port=6379)
           
            conn.ping()
            print ('      [+] Connected!\n')
        except Exception as ex:
            print ('      [+] Error:', ex,'\n')
            exit('        [+] Failed to connect, terminating.')


class MongoServe() :
    def __init__(self, isHost, isPort) :
        self.isHost = isHost
        self.isPort = isPort

    def CheckConnection(self):
        try:
            conn = MongoClient(self.isHost, int(self.isPort), connectTimeoutMS=3000)
            db = conn.list_database_names()
            print ('        [+] List Database in DB :', db)
            print ('        [+] Unauthenticated DB\n')
        except Exception as ex:
            print ('      [+] Error:', ex,'\n')
            exit('        [+] Failed to connect, terminating.')

    
# mongo = MongoServe('89.35.29.37', '27017')
# mongo.CheckConnection()