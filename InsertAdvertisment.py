from selenium import webdriver
import time
USERNAME='almatanjin'
PASSWORD='almatanjinalmatanjin'

driver=webdriver.Chrome(executable_path="C:\\Users\\ALMA TANJIN\\PycharmProjects\\Home_Rental_Management_System\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:8000/Insertadvertisment/")
userinput=driver.find_element_by_id('id_username')
userinput.send_keys(USERNAME)
passwordinput=driver.find_element_by_id('id_password')
passwordinput.send_keys(PASSWORD)
login_button=driver.find_element_by_id('login_id')
login_button.click()
house=driver.find_element_by_name('house')
driver.find_element_by_name('image1').send_keys("C://Users/ALMA TANJIN/PycharmProjects/To-Let-Too-Fast/media/images/Advertisement/s1.JPG")
driver.find_element_by_name('image2').send_keys("C://Users/ALMA TANJIN/PycharmProjects/To-Let-Too-Fast/media/images/Advertisement/s2.JPG")
button=driver.find_element_by_id('id')
button.click()


time.sleep(10)
driver.close()

print("succesful")