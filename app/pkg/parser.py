from bs4 import BeautifulSoup
import requests


url = 'https://lenta.ru/parts/news/'
r = requests.get(url)
r.raise_for_status()


soup = BeautifulSoup(r.content, "html.parser")
tag = soup.find_all("li", class_="parts-page__item")
for i in range(0,20):
    try:
        out = tag[i].find("h3").text + " "+ tag[i].find("time").text
        urlOut = "https://lenta.ru/parts/" + tag[i].find("a")['href']
    except AttributeError:
        print('end')