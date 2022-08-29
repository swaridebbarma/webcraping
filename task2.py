import json
from os import link
import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
response=requests.get(url)
Soup=BeautifulSoup(response.content,"html.parser")
def movie_data():
    movie_data=Soup.findAll("div",class_="lister-item mode-advanced")
    list=[]
    for store in movie_data:
        dic={}

        name=store.h3.a.text
        dic["Movie name"]=name

        year_of_release=store.h3.find("span",class_="lister-item-year text-muted unbold").get_text()[-5:-1]
        dic["Year"]=year_of_release

        runtime=store.p.find("span",class_="runtime").text.replace('min','')
        dic["Time"]=runtime

        meta=store.find("span",class_="metascore").text if store.find("span",class_="metascore") else'@'
        dic["Metascore"]=meta
        list.append(dic)

        a=store.find('div',class_="lister-item-content").a["href"]
        link="https://www.imdb.com/"+a
        dic["movie urls"]=link
        list.append(dic)
    with open ("task2.json","w") as f:
        json.dump(list,f,indent=4)
    return list
movie_data()