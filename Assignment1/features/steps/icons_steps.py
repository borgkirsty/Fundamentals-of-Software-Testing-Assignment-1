from behave import *
from selenium.webdriver.common.by import By
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
        "imageUrl": "https://www.product1.com/image.png",
        "postedBy": USERID,
        "priceInCents": 1000,},
    2: {
        "alertType": 2,
        "heading": "product2",
        "description": "product2 description",
        "url": "https://www.product2.com",
        "imageUrl": "https://www.product2.com/image.png",
        "postedBy": USERID,
        "priceInCents": 2000,},
    3: {
        "alertType": 3,
        "heading": "product3",
        "description": "product3 description",
        "url": "https://www.product3.com",
        "imageUrl": "https://www.product3.com/image.png",
        "postedBy": USERID,
        "priceInCents": 3000,},
    4: {
        "alertType": 4,
        "heading": "product4",
        "description": "product4 description",
        "url": "https://www.product4.com",
        "imageUrl": "https://www.product4.com/image.png",
        "postedBy": USERID,
        "priceInCents": 4000,},
    5: {
        "alertType": 5,
        "heading": "product5",
        "description": "product5 description",
        "url": "https://www.product5.com",
        "imageUrl": "https://www.product5.com/image.png",
        "postedBy": USERID,
        "priceInCents": 5000,},
    6: {
        "alertType": 6,
        "heading": "product6",
        "description": "product6 description",
        "url": "https://www.product6.com",
        "imageUrl": "https://www.product6.com/image.png",
        "postedBy": USERID,
        "priceInCents": 6000,}
}

#Test 5 -- Additional given as before but different when and then
@then(u'I should see 1 alerts')
def see_1alert(context):
    alerts = context.driver.find_elements(By.XPATH, '//main[@class="pb-3"]/table')
    assert len(alerts) == 1
    #raise NotImplementedError(u'STEP: Then I should see 1 alerts')

@given(u'I am an administrator of the website and I upload an alert of type 1')
def website_admin_and_upload_specific_alert_type1(context):
    #clear before tests
    requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')
    requests.post(URL, json = dummy_data[1])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload an alert of type 1')


@then(u'the icon displayed should be icon-car.png')
def type1_icon_displayed(context):
    icon = context.driver.find_element(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img')
    assert icon.get_attribute('src') == 'https://www.marketalertum.com/images/icon-car.png'
    #raise NotImplementedError(u'STEP: Then the icon displayed should be icon-car.png')


@given(u'I am an administrator of the website and I upload an alert of type 2')
def website_admin_and_upload_specific_alert_type2(context):
    #clear before tests
    requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')
    requests.post(URL, json = dummy_data[2])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload an alert of type 2')


@then(u'the icon displayed should be icon-boat.png')
def type2_icon_displayed(context):
    icon = context.driver.find_element(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img')
    assert icon.get_attribute('src') == 'https://www.marketalertum.com/images/icon-boat.png'
    #raise NotImplementedError(u'STEP: Then the icon displayed should be icon-boat.png')


@given(u'I am an administrator of the website and I upload an alert of type 3')
def website_admin_and_upload_specific_alert_type3(context):
    #clear before tests
    requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')
    requests.post(URL, json = dummy_data[3])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload an alert of type 3')


@then(u'the icon displayed should be icon-property-rent.jpg')
def type3_icon_displayed(context):
    icon = context.driver.find_element(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img')
    assert icon.get_attribute('src') == 'https://www.marketalertum.com/images/icon-property-rent.jpg'
    #raise NotImplementedError(u'STEP: Then the icon displayed should be icon-property-rent.jpg')


@given(u'I am an administrator of the website and I upload an alert of type 4')
def website_admin_and_upload_specific_alert_type4(context):
    #clear before tests
    requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')
    requests.post(URL, json = dummy_data[4])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload an alert of type 4')


@then(u'the icon displayed should be icon-property-sale.jpg')
def type4_icon_displayed(context):
    icon = context.driver.find_element(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img')
    assert icon.get_attribute('src') == 'https://www.marketalertum.com/images/icon-property-sale.jpg'
    #raise NotImplementedError(u'STEP: Then the icon displayed should be icon-property-sale.jpg')


@given(u'I am an administrator of the website and I upload an alert of type 5')
def website_admin_and_upload_specific_alert_type5(context):
    #clear before tests
    requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')
    requests.post(URL, json = dummy_data[5])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload an alert of type 5')


@then(u'the icon displayed should be icon-toys.png')
def type5_icon_displayed(context):
    icon = context.driver.find_element(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img')
    assert icon.get_attribute('src') == 'https://www.marketalertum.com/images/icon-toys.png'
    #raise NotImplementedError(u'STEP: Then the icon displayed should be icon-toys.png')


@given(u'I am an administrator of the website and I upload an alert of type 6')
def website_admin_and_upload_specific_alert_type6(context):
    #clear before tests
    requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')
    requests.post(URL, json = dummy_data[6])
    #raise NotImplementedError(u'STEP: Given I am an administrator of the website and I upload an alert of type 6')


@then(u'the icon displayed should be icon-electronics.png')
def type6_icon_displayed(context):
    icon = context.driver.find_element(By.XPATH, '//main[@class="pb-3"]/table/tbody/tr/td/h4/img')
    assert icon.get_attribute('src') == 'https://www.marketalertum.com/images/icon-electronics.png'
    #raise NotImplementedError(u'STEP: Then the icon displayed should be icon-electronics.png')

#clear site data
requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')