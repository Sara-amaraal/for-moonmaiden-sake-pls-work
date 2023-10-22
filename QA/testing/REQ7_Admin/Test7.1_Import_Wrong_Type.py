import sys
import unittest
import time
import logging #used so that every python module can be included/participate in the logging 
import os
from typing import final 
#The selenium.webdriver module provides all the WebDriver implementations. 
# Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote.
from selenium import webdriver
#The Keys class provide keys in the keyboard like RETURN, F1, ALT etc. 
from selenium.webdriver.common.keys import Keys
#WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.
#By default, WebDriverWait calls the ExpectedCondition every 500 milliseconds until it returns success
from selenium.webdriver.support.ui import WebDriverWait
#ExpectedCondition will return true (Boolean) in case of success or not null if it fails to locate an element.
from selenium.webdriver.support import expected_conditions as EC
#The By class is used to locate elements within a document.
from selenium.webdriver.common.by import By
#Set of default supported desired capabilities used as a starting point for requesting remote webdrivers for connecting to selenium server or selenium grid.
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#sets handlers for the logging system if the root logger doesn't have handlers configured
logging.basicConfig(filename="log.txt", level=logging.INFO)

#Melhorar com verificacoes
def login(driver):#driver refers to instance of webDriver
    
    driver.get("http://localhost:3000/login/")

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()

    username = "creator1"
    password = "password"

    #Username e password com as credenciais "creator1" e "password" para aceder como admin
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return

def test_import_wrong_type(driver):
    i = 0

    #admin access to navigation links
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a/b")))

    admin_button = driver.find_element(By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a/b")

    admin_button.click()

    PATH = os.getcwd()#Returns current working directory
    
    if PATH.endswith("quirked-up-software"):
        PATH += "\\DEV\\testing\\REQ7"
        os.chdir(PATH)

    elif PATH.endswith("DEV"):
        PATH += "\\testing\\REQ7"
        os.chdir(PATH)
    
    driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/div[1]/input").send_keys(os.getcwd()+"\\scary_type_import_test.pdf")

    import_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div[1]/button")
    import_button.click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    msg = alert.text

    #wrong type import recognised
    if msg.startswith("not well-formed"):
        i+=1

    alert.accept()
    
    return i


#PATH = "C:\Program Files (x86)\Chromedriver.exe" 
#Selenium can handle the browser and drivers by itself so we don´t need to use the path.

if __name__ == "__main__":
    driver = webdriver.Chrome()

    login(driver)
    if test_import_wrong_type(driver) == 1:
        print("Test7.1_Import_Wrong_Type.py is a SUCESS")
    else:
        print("Test7.1_Import_Wrong_Type.py failed :(")
    
    driver.close()

