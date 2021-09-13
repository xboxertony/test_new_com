import requests as req
from bs4 import BeautifulSoup

r = req.get("http://127.0.0.1:5500/test.html")

soup = BeautifulSoup(r.text,"html.parser")

for i in soup.find_all("div",class_="delta"):
    for j in i.select("a"):
        print(j.string)