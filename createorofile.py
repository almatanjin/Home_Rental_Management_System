from selenium import webdriver
import time
USERNAME='fahadahmed'
PASSWORD='FahadFahadFahad'

driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:8000/create-profile/")
userinput=driver.find_element_by_id('id_username')
userinput.send_keys(USERNAME)
passwordinput=driver.find_element_by_id('id_password')
passwordinput.send_keys(PASSWORD)
login_button=driver.find_element_by_id('login_id')
login_button.click()
driver.find_element_by_name('profile_picture').send_keys("C://Users/ALMA TANJIN/PycharmProjects/Selenium01p/media/fahad.JPG")
driver.find_element_by_name('contact_no').send_keys('880171807777')
driver.find_element_by_name('name').send_keys('Fahad Ahmed')
driver.find_element_by_name('email').send_keys('fahad.uap-bd.edu')
button=driver.find_element_by_id('id')
button.click()
time.sleep(10)
driver.get("http://127.0.0.1:8000/view-profile/")


time.sleep(10)
driver.close()

print("succesful")