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

def test_export(driver):
    i = 0

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a/b")))

    admin_button = driver.find_element(By.XPATH, "//*[@id=\"links_nav\"]/li[1]/a/b")
    admin_button.click()

    export_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div[2]/div/button")
    export_button.click()
    
    return i

#PATH = "C:\Program Files (x86)\Chromedriver.exe"
#we don´t need do specify the path as webdriver module already does that
if __name__ == "__main__":
    driver = webdriver.Chrome()

    login(driver)

    if test_export(driver) == 0:
        print("Test7.3_Export.py is a SUCESS")
    else:
        print("Test7.3_Export.py failed :(")
    
    driver.close()

