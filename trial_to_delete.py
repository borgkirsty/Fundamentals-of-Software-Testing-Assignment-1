import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests


USERID = '1f32da0b-e868-41d7-8a20-aa9cda53c09e'
URL = 'https://api.marketalertum.com/Alert'

#dummy data for testing
dummy_data = {
    1: {
        "alertType": 1,
        "heading": "product1",
        "description": "product1 description",
        "url": "https://www.product1.com",
        "imageUrl": "https://www.product1.com/image.jpg",
        "postedBy": USERID,
        "priceInCents": 1000,},
    2: {
        "alertType": 2,
        "heading": "product2",
        "description": "product2 description",
        "url": "https://www.product2.com",
        "imageUrl": "https://www.product2.com/image.jpg",
        "postedBy": USERID,
        "priceInCents": 2000,},
    3: {
        "alertType": 3,
        "heading": "product3",
        "description": "product3 description",
        "url": "https://www.product3.com",
        "imageUrl": "https://www.product3.com/image.jpg",
        "postedBy": USERID,
        "priceInCents": 3000,},
    4: {
        "alertType": 4,
        "heading": "product4",
        "description": "product4 description",
        "url": "https://www.product4.com",
        "imageUrl": "https://www.product4.com/image.jpg",
        "postedBy": USERID,
        "priceInCents": 4000,},
    5: {
        "alertType": 5,
        "heading": "product5",
        "description": "product5 description",
        "url": "https://www.product5.com",
        "imageUrl": "https://www.product5.com/image.jpg",
        "postedBy": USERID,
        "priceInCents": 5000,},
    6: {
        "alertType": 6,
        "heading": "product6",
        "description": "product6 description",
        "url": "https://www.product6.com",
        "imageUrl": "https://www.product6.com/image.jpg",
        "postedBy": USERID,
        "priceInCents": 6000,}
}


for i in range(1):
        #Sending POST request
        post= requests.post(URL, json = dummy_data[i+1])
        print(post.status_code)