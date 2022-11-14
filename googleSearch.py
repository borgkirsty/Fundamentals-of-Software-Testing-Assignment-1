from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


#To leave open after running
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


#Specify the path to the chromedriver.exe
driver = webdriver.Chrome(executable_path="C:\DRIVERS\Chromedriver\chromedriver.exe")
driver.implicitly_wait(10)

#Open the webpage
driver.get("https://www.google.com/")

#Accept the cookies
driver.find_element("id", "L2AGLb").click()
driver.implicitly_wait(10)

#Identify the search box and search for "Selenium"
box = driver.find_element("name","q")
box.send_keys("Selenium")
time.sleep(0.2) 
box.send_keys(Keys.RETURN)

