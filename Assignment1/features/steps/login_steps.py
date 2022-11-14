import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#Test 1
@given(u'I am a user of marketalertum')
def website_user(context):
    context.driver = webdriver.Chrome("C:\DRIVERS\Chromedriver\chromedriver.exe")
    context.driver.get("https://www.marketalertum.com")
    #raise NotImplementedError(u'STEP: Given I am a user of marketalertum')


@when(u'I login with valid credentials')
def valid_login(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='navbar-nav flex-grow-1']/li[3]/a"))).click()
    context.box = context.driver.find_element(By.ID, "UserId")
    context.box.send_keys("1f32da0b-e868-41d7-8a20-aa9cda53c09e")
    time.sleep(0.2) 
    context.box.send_keys(Keys.RETURN)
    #raise NotImplementedError(u'STEP: When I login with valid credentials')


@then(u'I should see my alerts')
def see_alerts(context):
    status = context.driver.find_element(By.XPATH, '//main[@class="pb-3"]/h1').is_displayed()
    assert status is True
    #raise NotImplementedError(u'STEP: Then I should see my alerts')

#Test 2 -- Same given as before but different when and then
@when(u'I login with invalid credentials')
def invalid_login(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='navbar-nav flex-grow-1']/li[3]/a"))).click()
    context.box = context.driver.find_element(By.ID, "UserId")
    context.box.send_keys("invalid_credentials")
    time.sleep(0.2) 
    context.box.send_keys(Keys.RETURN)
    #raise NotImplementedError(u'STEP: When I login with invalid credentials')


@then(u'I should see the login screen again')
def see_login_screen(context):
    status = context.driver.find_element(By.ID, "UserId").is_displayed()
    assert status is True
    #raise NotImplementedError(u'STEP: Then I should see the login screen again')

