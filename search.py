import requests, sys, json

class Search():
    def __init__(self, isMurmur, isKey):
        self.isMurmur = isMurmur
        self.isKey = isKey

    def FaviconHash(self):
        mumurhash = "http.favicon.hash:"+str(self.isMurmur)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
            url = "https://api.shodan.io/shodan/host/search?key="+str(self.isKey)+"&query="+str(mumurhash)
            req = requests.get(url, headers)
            if req.status_code == 200 :
                return json.loads(req.text)
            else :
                print ("[+] Oops Connections is close ")
                sys.exit(1)
        except : 
            print ("[+] Oops Connections is close ")
            sys.exit(1)