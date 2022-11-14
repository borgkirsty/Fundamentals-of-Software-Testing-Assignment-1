import json
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#Constants
USERID = '1f32da0b-e868-41d7-8a20-aa9cda53c09e'
URL = 'https://api.marketalertum.com/Alert'
E_COMMERCE_URL = 'https://www.scanmalta.com/shop/'
QUERY = 'Laptops'

def settingUpDriver():
    #To leave open after running
    myOptions = Options()
    myOptions.add_experimental_option("detach", True)

    #Set up Services
    myService = Service("C:\DRIVERS\Chromedriver\chromedriver.exe")

    #Set up Driver
    driver = webdriver.Chrome(service=myService, options=myOptions)

    return driver

def searchWebPage(driver, url, query):
    #Open the webpage
    driver.get(url)


    #Identify the search box and search for "Laptops"
    searchBox = driver.find_element("id","search")
    searchBox.send_keys(query)
    time.sleep(0.2)
    searchBox.send_keys(Keys.RETURN)


#Scraping Part

def retrieveData(driver):
    #Locators
    product_name = driver.find_elements(By.XPATH,'(//li[@class="item product product-item"]/div/div[2]/strong/a)[position()<=5]')
    product_price = driver.find_elements(By.XPATH,'(//li[@class="item product product-item"]/div/div[2]/div[2]/span/span/span[2][contains(@data-price-type,"finalPrice")]/span)[position()<=5]')
    product_image = driver.find_elements(By.XPATH,'(//li[@class="item product product-item"]/div/div/a/span/span/img[contains(@class,"product-image-photo main-img")])[position()<=5]')

    return product_name, product_price, product_image

def createJson(product_name, product_price, product_image):
    #Storing element in nested dictionary
    products = {}
    for i in range(len(product_name)):
        products[i+1] = {
            "alertType": 6,
            "heading": product_name[i].text,
            "description": product_name[i].text,
            "url": product_name[i].get_attribute("href"),
            "imageUrl": product_image[i].get_attribute("src"), #Image will not appear as the e-commerce site does not allow hotlinking to images
            "postedBy": USERID,
            "priceInCents": re.sub("[^0-9]", "", product_price[i].text)
        }
    return products

    #print(json.dumps(products, indent = 4))

def sendJson(products, product_name):
    #initialise empty list to store the response
    response = []
    for i in range(len(product_name)):
        #Sending POST request
        post = requests.post(URL, json = products[i+1])
        response.append(post.status_code)
        #print(x.status_code)
    
    return response

def main():
    #Setting up driver
    driver = settingUpDriver()

    #Searching for Laptops
    searchWebPage(driver, E_COMMERCE_URL, QUERY)

    #Retrieving data
    product_name, product_price, product_image = retrieveData(driver)

    #Creating JSON
    products = createJson(product_name, product_price, product_image)

    #Sending JSON
    sendJson(products,product_name)

    driver.quit()

if __name__ == "__main__":
    main()