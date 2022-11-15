import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import validators
from jsonschema import validate

from scraper import *

class Tests(unittest.TestCase):

    #initializing the driver
    def setUp(self):
        self.driver = webdriver.Chrome()

    #test if there are search results
    def test_search_results(self):

        #test where results are found
        found = searchWebPage(self.driver, "https://www.scanmalta.com/shop/", "Laptops")
        self.assertTrue(found)

        #test where no results are found
        notfound = searchWebPage(self.driver, "https://www.scanmalta.com/shop/", "xyzabc")
        self.assertFalse(notfound)
    
    #test the data retrieved
    def test_retrieveData(self):
        
        #test that no data is retrieved
        searchWebPage(self.driver, "https://www.scanmalta.com/shop/", "xyzabc")
        self.assertEqual(retrieveData(self.driver), ([], [], []))

        #test if the data is retrieved
        searchWebPage(self.driver, "https://www.scanmalta.com/shop/", "Laptops")
        self.assertNotEqual(retrieveData(self.driver), ([], [], []))

        #test if the correct ammount of data is retrieved -- driver is currently in the laptops search results page
        name, price, image = retrieveData(self.driver)
        self.assertEqual(len(name), 5)
        self.assertEqual(len(price), 5)
        self.assertEqual(len(image), 5)

        #test if the data type is correct
        for i in range(len(name)):
            self.assertIsInstance(name[i].text, str)
            self.assertIsInstance(price[i].text, str)
            self.assertIsInstance(image[i].text, str)
            self.assertTrue(validators.url(image[i].get_attribute("src")))
            self.assertTrue(validators.url(name[i].get_attribute("href")))

    #test the json created
    def test_createJson(self):

        #schema for JSON
        schema = {
            "1" : {
                "alertType": 6,
                "heading": "string",
                "description": "string",
                "url": "string",
                "imageUrl": "string",
                "postedBy": "string",
                "price": "string"
            },
            "2" : {
                "alertType": 6,
                "heading": "string",
                "description": "string",
                "url": "string",
                "imageUrl": "string",
                "postedBy": "string",
                "price": "string"
            }, 
            "3" : {
                "alertType": 6,
                "heading": "string",
                "description": "string",
                "url": "string",
                "imageUrl": "string",
                "postedBy": "string",
                "price": "string"
            },
            "4" : {
                "alertType": 6,
                "heading": "string",
                "description": "string",
                "url": "string",
                "imageUrl": "string",
                "postedBy": "string",
                "price": "string"
            },
            "5" : {
                "alertType": 6,
                "heading": "string",
                "description": "string",
                "url": "string",
                "imageUrl": "string",
                "postedBy": "string",
                "price": "string"
            }
        }

        #test if the json is created
        searchWebPage(self.driver, "https://www.scanmalta.com/shop/", "Laptops")
        name, price, image = retrieveData(self.driver)
        json = createJson(name, price, image)
        self.assertFalse(validate(json, schema))

    #test post request
    def test_post(self):
        #test if the post request is successful
        searchWebPage(self.driver, "https://www.scanmalta.com/shop/", "Laptops")
        name, price, image = retrieveData(self.driver)
        json = createJson(name, price, image)
        x = sendJson(json, name)
        for i in range(len(name)):
            self.assertEqual(x[i], 201)

       # requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')        

        #test if the post request is unsuccessful
        fake_json = {
                "alertType": 6,
                "heading": "Heading",
                "description": "Description",
                "imageUrl": "URL",
                "postedBy": "xyz123"
            }
        y = requests.post(URL, json = fake_json)
        #Checking if the request was unsuccessful
        #self.assertEqual(y.status_code, 400)
        self.assertNotEqual(y.status_code, 201)

        requests.delete('https://api.marketalertum.com/Alert?userId=1f32da0b-e868-41d7-8a20-aa9cda53c09e')        


    #closing the driver
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()