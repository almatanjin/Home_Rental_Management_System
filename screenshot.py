from selenium import webdriver

from selenium.webdriver.common.by import By

import time

from PIL import Image ## pip install Pillow

driver = webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()

driver.get("http://127.0.0.1:8000/accounts/login/")

time.sleep(2)

driver.save_screenshot("image.png")

# Loading the image

image = Image.open("image.png")