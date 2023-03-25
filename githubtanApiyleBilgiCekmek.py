import requests


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com' #github un api linki
        self.token = 'jsdnıkusıjaujawvnaevn564gw5wg55gw' # kafadan salladım
        
        
        
    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+ username) # api_url nin sonuna users ve dişarıdan aldığımız username bilgilerini ekliyoruz
        return response.json() # response yi json listeye donüstürür
        
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+ username+'/repos') # ayriyeten repos(attığı döküman) bilgisini alıyor 
        return response.json()
    
    def createRepository(self, name): # sonuc vermiyecek ama yol aynı token salladım
        response = requests.post(self.api_url+'/user/repos?acces_token'+self.token, json={ # bilgi verirken post dememiz gerekiyor.
            "name": "Hello-word",
            "description": "This is your first repository",
            "homepage": "https://github.com"
            })
        return response.json()
github = Github()


while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ")
    
    if secim == "4":
        break
    else:
        if secim == "1":
            username= input('username:')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        elif secim == "2":
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == "3":  # repository yeni dökuman=proje oluşturma 
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print("yanliş seçim yaptınız")