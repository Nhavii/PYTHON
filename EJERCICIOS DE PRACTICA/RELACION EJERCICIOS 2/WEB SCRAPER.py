import requests
from bs4 import BeautifulSoup

url="http://books.toscrape.com"
response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")

titulares=soup.find_all("h1")

for titular in titulares:
    print(titular.text)

