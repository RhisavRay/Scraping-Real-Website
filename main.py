from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.nike.com/in/w/mens-running-shoes-37v7jznik1zy7ok').text

soup = BeautifulSoup(html_text, 'lxml')

productCards = soup.find_all('div', class_ = 'product-card')

productLinks = []
for productCard in productCards:
    productLink = productCard.find('a', class_ = 'product-card__link-overlay')
    productLinks.append(productLink['href'])

print(productLinks)