from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()

#driver.get('http://www.saucedemo.com')
driver.maximize_window()
#user_name=driver.find_element(By.XPATH,'//input[@id="user-name"]')
#//div[@class="form_group"][1]
#//h4[text()="Password for all users:"]
#//h4[contais(text(),"Password"]
#login="standard_user"
#user_name.send_keys(login)
#sleep(5)

driver.get('http://lambdatest.com')
user_message=driver.find_element(By.ID,'user-message')
sleep(5)
#Найти элемент по XPATH с помощью Selenium в Python можно скопировав по XPATH  через devtools.

chec_all=driver.find_element(By.XPATH,'//*[@id="box"]')