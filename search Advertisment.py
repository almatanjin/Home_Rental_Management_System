from selenium import webdriver
import time
USERNAME='almatajin'
PASSWORD='almatajinalmatajin'
driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")


driver.maximize_window()
driver.get("http://127.0.0.1:8000/Advertisment")
userinput=driver.find_element_by_id('id_username')
userinput.send_keys(USERNAME)
passwordinput=driver.find_element_by_id('id_password')
passwordinput.send_keys(PASSWORD)
login_button=driver.find_element_by_id('login_id')
login_button.click()
search=driver.find_element_by_name('search')
search.send_keys("Banani")
time.sleep(5)
search_button=driver.find_element_by_id('search')
search_button.click()
detail_button=driver.find_element_by_id('id')
time.sleep(5)
detail_button.click()
time.sleep(20)
driver.close()