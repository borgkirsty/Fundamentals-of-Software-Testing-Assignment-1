import time
from behave import *
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

#Test 3 -- Same given as before but additional but different when and then
@given(u'I am an administrator of the website and I upload 3 alerts')
def website_admin_and_upload3(context):
    for i in range(3):
        #Sending POST request
        requests.post(URL, json = dummy_data[i+1])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload 3 alerts')


@when(u'I view a list of alerts')
def view_alerts_list(context):
    #context.execute_steps(u'''I login with valid credentials''')
    #Copy and paste the code from the previous test
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='navbar-nav flex-grow-1']/li[3]/a"))).click()
    context.box = context.driver.find_element(By.ID, "UserId")
    context.box.send_keys("1f32da0b-e868-41d7-8a20-aa9cda53c09e")
    time.sleep(0.2) 
    context.box.send_keys(Keys.RETURN)
    #raise NotImplementedError(u'STEP: When I view a list of alerts')


@then(u'each alert should contain an icon')
def alert_contains_icon(context):
    icons = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img')
    assert len(icons) == 3
    #raise NotImplementedError(u'STEP: Then each alert should contain an icon')


@then(u'each alert should contain a heading')
def alert_contains_heading(context):
    heading = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img') #Same XPATH as icons
    assert len(heading) == 3
    #raise NotImplementedError(u'STEP: Then each alert should contain a heading')


@then(u'each alert should contain a description')
def alert_contains_description(context):
    description = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr[3]/td')
    assert len(description) == 3
    #raise NotImplementedError(u'STEP: Then each alert should contain a description')


@then(u'each alert should contain an image')
def alert_contains_image(context):
    image = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr[2]/td/img')
    assert len(image) == 3
    #raise NotImplementedError(u'STEP: Then each alert should contain an image')


@then(u'each alert should contain a price')
def alert_contains_price(context):
    price = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr[4]/td/b')
    assert len(price) == 3
    #raise NotImplementedError(u'STEP: Then each alert should contain a price')


@then(u'each alert should contain a link to the original product website')
def alert_contains_originalURL(context):
    originalURL = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr[5]/td/a')
    assert len(originalURL) == 3
    #raise NotImplementedError(u'STEP: Then each alert should contain a link to the original product website')


#Test 4 -- Additional given as before but different when 
@given(u'I am an administrator of the website and I upload more than 5 alerts')
def website_admin_and_uploadExtra(context):
    for i in range(len(dummy_data)):
        #Sending POST request
        requests.post(URL, json = dummy_data[i+1])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload more than 5 alerts')


@when(u'I view a list of alerts I should see 5 alerts')
def view_alerts_list_see5(context):
    #context.execute_steps(u'''I login with valid credentials''')
    #Copy and paste the code from the previous test
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='navbar-nav flex-grow-1']/li[3]/a"))).click()
    context.box = context.driver.find_element(By.ID, "UserId")
    context.box.send_keys("1f32da0b-e868-41d7-8a20-aa9cda53c09e")
    time.sleep(0.2) 
    context.box.send_keys(Keys.RETURN)
    alerts = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table')
    assert len(alerts) == 5
    #raise NotImplementedError(u'STEP: When I view a list of alerts I should see 5 alerts')


#clear site data
requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')