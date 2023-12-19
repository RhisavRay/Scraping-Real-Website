from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

mainSiteUrl = 'https://www.nike.com/in/w/mens-running-shoes-37v7jznik1zy7ok'

# Using selenium to load the page
driver = webdriver.Chrome()
driver.get(mainSiteUrl)

# Wait for the product card to be present
wait = WebDriverWait(driver, 10)
productCards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-card')))

productInfo = []

for productCard in productCards:
    imgUrl = productCard.find_element(By.CLASS_NAME, 'product-card__hero-image').get_attribute('src')

    name = productCard.find_element(By.CLASS_NAME, 'product-card__title').text

    price = productCard.find_element(By.CLASS_NAME, 'product-price').text[6:]

    info = {'name': name, 'price': price, 'imgUrl': imgUrl}

    productInfo.append(info)

driver.quit()

with open('nikeData.json', 'w') as jsonFile:
    json.dump(productInfo, jsonFile, indent = 2)

print("Data saved to new JSON file!")