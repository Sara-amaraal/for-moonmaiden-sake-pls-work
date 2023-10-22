import sys
import unittest
import time
import logging
import os
from typing import final 
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
logging.basicConfig(filename="log.txt", level=logging.INFO)

#Melhorar com verificacoes
def login(driver):
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()

    username = "creator1"
    password = "password"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return

def test_import_right_type(driver):
    i = 0

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a/b")))

    admin_button = driver.find_element(By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a/b")

    admin_button.click()

    PATH = os.getcwd()
    
    if PATH.endswith("quirked-up-software"):
        PATH += "\\DEV\\testing\\REQ7"
        os.chdir(PATH)

    elif PATH.endswith("DEV"):
        PATH += "\\testing\\REQ7"
        os.chdir(PATH)
    
    driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/div[1]/input").send_keys(os.getcwd()+"\\good_type_import_test.xml")

    import_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div[1]/button")
    import_button.click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    msg = alert.text

    if msg == "Quizzes read successfully!":
        i+=1

    alert.accept()
    
    return i

#PATH = "C:\Program Files (x86)\Chromedriver.exe"
#We don't need to specify the path as the webdriver module already does that
if __name__ == "__main__":
    driver = webdriver.Chrome()

    login(driver)

    if test_import_right_type(driver) == 1:
        print("Test7.2_Import_Right_Type.py is a SUCESS")
    else:
        print("Test7.2_Import_Right_Type.py failed :(")
    
    driver.close()

