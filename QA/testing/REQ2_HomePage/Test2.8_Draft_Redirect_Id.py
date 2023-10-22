"""
Automated Testing Script for 'Draft Redirect' Functionality on the Web Application using the Selenium library

Usage:
    1. Having Selenium installed.
    2. Provide an appropriate Chrome WebDriver executable (chromedriver.exe) in the PATH.
    3. Set the 'username' and 'password' variables with valid login credentials.

The script consists of the following functions:
    - login(driver): Logs into the web application.
    - test_draft(driver): Tests the "Draft Redirect" functionality.

Script Execution:
    When executed, the script performs the following steps:
    1. Opens a Chrome browser using the WebDriver.
    2. Logs in to the web application using the provided credentials.
    3. Tests the "Draft Redirect" functionality.
    4. Prints a success message if the test is successful; otherwise, it prints a failure message.
    5. Properly closes the WebDriver.

"""
import sys
import unittest
import time
import logging
from typing import final
from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
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

    # TODO alterar para um user que seja solver
    username = "creator1"
    password = "password"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return


def test_draft(driver):
    """
    Tests the "Draft Redirect" functionality of the web application by hitting 'Save' in a Quiz instead of 'Submit'.
    Result must be being redirected to the 'expected_link'.

    Args:
        driver (WebDriver): Selenium WebDriver

    Returns:
        int: 1 if the test is successful, 0 otherwise
    """
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "Solve_button"))
    )

    draft = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div/main/div[1]/div[1]/a'
    )

    if draft == None:
        return 1

    draft.click()

    expected_url = "http://localhost:3000/create-quizz/"

    current_url = driver.current_url

    if expected_url in current_url:
        return 1

    return 0


PATH = "C:\Program Files (x86)\Chromedriver.exe"

if __name__ == "__main__":
    driver = webdriver.Chrome(PATH)

    login(driver)

    if test_draft(driver) == 1:
        print("Test2.8_Draft_Redirect_Id.py is a SUCESS")
    else:
        print("Test2.8_Draft_Redirect_Id.py failed :(")

    driver.close()
