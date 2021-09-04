from selenium import webdriver
import time
USERNAME='almatajin'
PASSWORD='almatajinalmatajin'
driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:8000/accounts/login/")
userinput=driver.find_element_by_id('id_username')
userinput.send_keys(USERNAME)
passwordinput=driver.find_element_by_id('id_password')
passwordinput.send_keys(PASSWORD)
login_button=driver.find_element_by_id('login_id')
login_button.click()

time.sleep(10)
driver.close()
driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")


driver.maximize_window()
driver.get("http://127.0.0.1:8000/Home")
time.sleep(10)
driver.close()
print("succesful")
