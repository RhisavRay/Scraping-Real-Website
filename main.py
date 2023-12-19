from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.nike.com/in/w/mens-running-shoes-37v7jznik1zy7ok').text

soup = BeautifulSoup(html_text, 'lxml')

productLinks = soup.find_all('a', class_ = 'product-card__img-link-overlay')

print(productLinks)