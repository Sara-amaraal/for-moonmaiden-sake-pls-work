"""
Automated Testing Script for 'Profile' Button Functionality on the Web Application using the Selenium library

Usage:
    1. Having Selenium installed.
    2. Provide an appropriate Chrome WebDriver executable (chromedriver.exe) in the PATH.
    3. Set the 'username' and 'password' variables with valid login credentials.

The script consists of the following functions:
    - login(driver): Logs into the web application.
    - profile(driver): Tests the "Profile" button.

Script Execution:
    When executed, the script performs the following steps:
    1. Opens a Chrome browser using the WebDriver.
    2. Logs in to the web application using the provided credentials.
    3. Tests the "Profile" button.
    4. Prints a success message if the test is successful; otherwise, it prints a failure message.
    5. Properly closes the WebDriver.

"""
import sys
import unittest
import time
import logging
from typing import final
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

logging.basicConfig(filename="log.txt", level=logging.INFO)


# Melhorar com verificacoes
def login(driver):
    """
    Logs into the web application.

    Args:
        driver (WebDriver): Selenium WebDriver
    Returns:
        _type_: None
    """
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    username = "justAUser1"
    password = "admin123"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return


def profile(driver):
    """
    Tests the "Profile" button on the web application.
    Result must be being redirected to the 'expected_link'.

    Args:
        driver (WebDriver): Selenium WebDriver

    Returns:
        int: 1 if the test is successful, 0 otherwise
    """
    i = 0
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="links_nav"]/li[6]/a/b'))
    )

    profile_button = driver.find_element(By.XPATH, '//*[@id="links_nav"]/li[6]/a/b')

    profile_button.click()

    time.sleep(1)

    expected_url = "http://localhost:3000/profile"

    current_url = driver.current_url

    if current_url == expected_url:
        i += 1

    return i


PATH = "C:\Program Files (x86)\Chromedriver.exe"

if __name__ == "__main__":
    driver = webdriver.Chrome(PATH)

    login(driver)

    if profile(driver) == 1:
        print("Test2.4_Profile_Button.py is a SUCESS")
    else:
        print("Test2.4_Profile_Button.py failed :(")

    driver.close()
