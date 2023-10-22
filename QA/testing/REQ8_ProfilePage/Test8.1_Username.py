import time
import logging
from typing import final 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
logging.basicConfig(filename="log.txt", level=logging.INFO)



#login as an user
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
    login_button.click()
    return username

def goto_Profile(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[6]/a")))
    profile_button = driver.find_element(By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[6]/a")
    profile_button.click()

    expected_url = "http://localhost:3000/profile"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Create Quiz button")
        return False

    return True

def test_username():
    driver = webdriver.Chrome(ChromeDriverManager().install()) # or driver = webdriver.Chrome('./chromedriver')
    user = login(driver)
    goto_Profile(driver)
    
    username = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/main/header/nav/div[2]/p").text

    if (user == username):
        return True
    
    

if __name__ == "__main__":
    if test_username() == True:
        print("Test8.1_Username.py is a SUCESS")
    else:
        print("Test8.1_Username.py failed :(")