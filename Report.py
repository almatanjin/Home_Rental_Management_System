from selenium import webdriver

import unittest

import HTMLTestRunner ## pip install html-testRunner in command line

from selenium.webdriver.common.by import By

class TestReport(unittest.TestCase):

@classmethod

def setUpClass(cls):

cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Fahad
Ahmed\\PycharmProjects\\SeleniumProject01\\drivers\\chromedriver.exe")

cls.driver.implicitly_wait(2)

def test_search_one(self):

self.driver.get("https://opensource-demo.orangehrmlive.com/")

self.driver.find_element(By.LINK_TEXT,"Forgot your password?").click()

def test_search_two(self):

self.driver.get("https://opensource-demo.orangehrmlive.com/")

self.driver.find_element(By.LINK_TEXT, "Forgot your").click()

@classmethod

def tearDownClass(cls):

cls.driver.close()

cls.driver.quit()

print("Test Completed")

if __name__ == '__main__':

unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='C:/Users/Fahad
Ahmed/PycharmProjects/SeleniumProject01/Reports'))