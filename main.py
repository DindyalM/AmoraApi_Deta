import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    url='https://www.fashionnova.com/collections/dresses'
    count = 0
    a =[]
    #grab our main links
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    dress_divs = soup.find_all('div', class_='collection-list__product-tile')
    for div in dress_divs:
        count = count  + 1
        a.append(div.find('a').attrs['href'])
        if(count==5):break

    return {a[0]}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}




