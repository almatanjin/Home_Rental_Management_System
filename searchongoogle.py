from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
userinput=driver.find_element_by_name('q')
userinput.send_keys("UAP")

userinput.send_keys(Keys.ENTER)