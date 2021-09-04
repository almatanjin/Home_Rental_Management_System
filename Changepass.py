from selenium import webdriver
import time
USERNAME='almatajin1088'
PASSWORD='almatajinalmatajinalma'
PASSWORD11='almatajinalmatajinalma11'
driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:8000/accounts/password_change/")
userinput=driver.find_element_by_id('id_username')
userinput.send_keys(USERNAME)
passwordinput=driver.find_element_by_id('id_password')
passwordinput.send_keys(PASSWORD)
login_button=driver.find_element_by_id('login_id')
login_button.click()
userinput=driver.find_element_by_name('old_password')
userinput.send_keys(PASSWORD)
passwordinput=driver.find_element_by_name('new_password1')
passwordinput.send_keys(PASSWORD11)
passwordinput=driver.find_element_by_name('new_password2')
passwordinput.send_keys(PASSWORD11)
# check_button=driver.find_element_by_id('landlord')
button=driver.find_element_by_id('id')
button.click()


time.sleep(10)
driver.close()

print("succesful")