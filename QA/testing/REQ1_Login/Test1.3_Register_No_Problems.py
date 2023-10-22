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
import random
import string

logging.basicConfig(filename="log.txt", level=logging.INFO)

##TODO TESTAR REGISTER!!
##Neste teste, Username existente com password diferente

PATH = "C:\Program Files (x86)\Chromedriver.exe"

def no_problem():
    i = 0

    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception ("Unable to load Login Page")

    driver.maximize_window()
    
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    register_button = driver.find_element(By.ID, "register")
    register_button.click()

    time.sleep(1)

    expected_url = "http://localhost:3000/"

    current_url = driver.current_url

    if (current_url == expected_url or current_url == "http://localhost:3000"):
        i+=1

    driver.close()
    return i

if __name__ == "__main__":
    if no_problem() == 1:
        print("Test1.3_Register_No_Problems.py is a SUCESS")
    else:
        print("Test1.3_Register_No_Problems.py failed :(")