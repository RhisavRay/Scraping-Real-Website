from bs4 import BeautifulSoup
import requests
import json

mainSite = requests.get('https://www.nike.com/in/w/mens-running-shoes-37v7jznik1zy7ok').text
soup = BeautifulSoup(mainSite, 'lxml')

productInfo = []

productCards = soup.find_all('div', class_ = 'product-card')

for productCard in productCards:
    imgUrl = productCard.find('img', class_ = 'product-card__hero-image')['src']
    # print(imgUrl)

    name = productCard.find('div', class_ = 'product-card__title').text
    # print(name)

    price = productCard.find('div', class_ = 'product-price').text[6:]
    # print(price)

    info = {'name': name, 'price': price, 'imgUrl': imgUrl}

    productInfo.append(info)

print(productInfo)