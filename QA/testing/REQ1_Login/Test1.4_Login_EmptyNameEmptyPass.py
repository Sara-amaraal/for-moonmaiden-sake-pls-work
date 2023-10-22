import sys
import unittest
import time
import logging
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
logging.basicConfig(filename="log.txt", level=logging.INFO)

##TODO TESTAR login!!
##Neste teste, username vazio ou password vazia

PATH = "C:\Program Files (x86)\Chromedriver.exe"

def empty_name_empty_pass():
    i = 0

    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()
    
    username = "creator1"
    password = "password"
    vazia = ""

    
    #USERNAME E PASS VAZIOS

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(vazia)
    driver.find_element(By.ID, "pass").send_keys(vazia)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-login")))

    time.sleep(1)
    alert = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/p')

    if (alert.text == "Invalid Credentials!"):
        i+=1
        
    
    #USERNAME VÁLIDO E PASS VAZIA
    driver.refresh()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(vazia)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-login")))

    time.sleep(1)
    alert = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/p')

    if (alert.text == "Invalid Credentials!"):
        i+=1

    
    #USERNAME VAZIO E PASS VÁLIDA
    driver.refresh()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(vazia)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "form-login")))

    time.sleep(1)
    alert = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/p')

    if (alert.text == "Invalid Credentials!"):
        i+=1

    driver.close()
    return i

if __name__ == "__main__":
    if empty_name_empty_pass() == 3:
        print("Test1.4_Login_EmptyNameEmptyPass.py is a SUCESS")
    else:
        print("Test1.4_Login_EmptyNameEmptyPass.py failed :(")