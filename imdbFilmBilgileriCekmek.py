import requests
from bs4 import BeautifulSoup



url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250" # imdb.com sitesinin en cok oy alan linki

html = requests.get(url).content # sayfa url sini içe aktarıyoruz Response 200 gelirse başarılıdır.
#content = response.content # url sayfasındaki bütün htm kodları gelir.bir üst kodda daha kolay ilişkilendirdik.

soup = BeautifulSoup(html, "html.parser") # sayfayı html kodu olduğunu söyler.

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr", limit=100)# tbody (tabloyu) çağırıyoruz ama class ı lister-list olan tabloyu. ve find_all ile tr leri seçiyoruz 250 tane tr gelir. ve limit=1 dediğimizde 1 tane tr gelir.


count = 1 # birinci ikinçi film diye gisecek

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text  # for dongüsüyle tr içerisinde find ile td bilgilerini alırız class ı title column olanları ve a etiketi iiçinden text bilgisini. biz başlık, isim ve beğenme sayısını alıcaz.
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()") # yıl bilgisini aldık yukarıdaki gibi ve yıldaki parantez bilgilerini de .strip("()") methoduyla kaldırdık.
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text # reating bilgisini veriri strong içinden text alır



    print(f"{count}- film: {title.ljust(56)} yıl: {year.ljust(8)} değerlendirme: {rating}")
    count+=1