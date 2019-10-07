import requests
import mmh3
import base64
import sys

class Favicon():
    def __init__(self, isURI):
        self.isURI = isURI

    def GetFavicon(self):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
            # masih menggunakan default url /favicon.ico, the next version akan dibikin automation
            icon = requests.get(self.isURI, verify=True)
            if icon.status_code == 200:
                favicon2 = base64.encodestring(icon.content)
                hash = mmh3.hash(favicon2)
                return hash
            else : 
                print ("Opsss /favicon.ico not found")
                sys.exit(1)
        except Exception as ex : 
            print ("Opss something erorr", ex)
            sys.exit(1)
