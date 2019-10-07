#!/usr/bin/python3

from favicon import Favicon
from search import Search
import sys
import socket
import configparser
import json
from serve import RedisServe, MongoServe
import argparse


config = configparser.ConfigParser()
config.read('config')
shodantoken = config['TOKEN']['shodan_key']
listPort =  json.loads(config.get("PORT", "list"))


def isOpenPort(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()


def getOpenPortList(ip):
    for el in listPort:
        if isOpenPort(ip, el.split('/')[0]):
            try:
                MESSAGE = "    [WARNING] >>>>> IP : "+ ip +" PORT : "+ el +" is Accessible  From Public"
                print(MESSAGE)
                # handling serve 
                if (el.split('/')[1] == "redis"):
                    redis = RedisServe(ip)
                    redis.CheckConnection()
                
                if (el.split('/')[1] == "mongodb"):
                    isPort = int(el.split('/')[0])
                    mongo = MongoServe(ip, isPort)
                    mongo.CheckConnection()

            except :
                pass
            
def extract_response(response):
    
    try :
        for res in (response['matches']):
            ipAddr   = res['ip_str']
            portDefault = res['port']
            print ("\n\n[INFO] IP  : ",ipAddr, " Port : ", portDefault)
            print ("[!] Scan Common Port .... ")
            getOpenPortList(ipAddr)
    except:
        print ("errors")
        sys.exit(1)
        pass
        

def main():
    parser = argparse.ArgumentParser(description='My example explanation')
    
    parser.add_argument('--mmh', help='provide an mumur hash : ./shodan.py --mmh=121231222')
    parser.add_argument('--fav', help='favicon url localtion : ./shodan.py --fav=https://localhost/favicon.ico')
    args = parser.parse_args()
    
    if args.mmh:
        search = Search(args.mmh, shodantoken)
        response = search.FaviconHash()
        print ("[+] Searching for mumurhash : ", args.mmh)
        extract_response(response)
        print ("[+] Finished !!!!")
    if args.fav :
        Fav = Favicon(str(args.fav))
        mumur = Fav.GetFavicon()
        print ("[INFO] Murmur hash of favicon should be ", mumur)
        search = Search(mumur, shodantoken)
        response = search.FaviconHash()
        extract_response(response)
        print ("[+] Finished !!!!")

if __name__ == "__main__":
     main()