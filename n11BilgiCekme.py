import requests
from bs4 import BeautifulSoup


url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"


html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")


list = soup.find_all("li", {"class":"column"})  # ,limit=5


for li in list:
    name = li.div.a.h3.text.strip() # bilgisayarın name i alır
    link = li.div.a.get("href")  # bilgisayarım-n linkini alır
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL') # eski fiyatı verir
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL') # yeni fiyatı verir    
    
    print(f"Bilgisayarın ismi: {name} link: {link} Eski fiyatı: {oldprice} Yeni fiyatı: {newprice}")
    print("*"*100)
