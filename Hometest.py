from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")


driver.maximize_window()
driver.get("https://github.com/almatanjin")

time.sleep(5)
driver.get("https://www.uap-bd.edu")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.close()
print("succesful")