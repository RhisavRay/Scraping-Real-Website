from bs4 import BeautifulSoup
import requests

mainSite = requests.get('https://www.nike.com/in/w/mens-running-shoes-37v7jznik1zy7ok').text
soup = BeautifulSoup(mainSite, 'lxml')

productCards = soup.find_all('div', class_ = 'product-card')

for productCard in productCards:
    productLink = productCard.find('a', class_ = 'product-card__link-overlay')['href']

    productSite = requests.get(productLink).text
    soup = BeautifulSoup(productSite, 'lxml')
    print(soup)