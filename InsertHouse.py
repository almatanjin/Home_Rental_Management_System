from selenium import webdriver
import time
USERNAME='almatanjin'
PASSWORD='almatanjinalmatanjin'

driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:8000/InsertHouse/")
userinput=driver.find_element_by_id('id_username')
userinput.send_keys(USERNAME)
passwordinput=driver.find_element_by_id('id_password')
passwordinput.send_keys(PASSWORD)
login_button=driver.find_element_by_id('login_id')
login_button.click()
address=driver.find_element_by_name('address')
driver.find_element_by_name('size_in_sqfeet').send_keys('450')
driver.find_element_by_name('rent').send_keys('25000')
driver.find_element_by_name('room_no').send_keys('4')
driver.find_element_by_name('image').send_keys("C://Users/ALMA TANJIN/PycharmProjects/Selenium01p/media/home.JPG")
button=driver.find_element_by_id('id')
button.click()


time.sleep(10)
driver.close()

print("succesful")