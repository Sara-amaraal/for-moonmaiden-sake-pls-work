"""
Automated Testing Script for 'Buttons in review quiz' functionality of the Web Application using the Selenium library

Usage:
    1. Having Selenium installed.
    2. Having webdriver_manager installed (pip install webdriver-manager)
    3. Set the 'username' and 'password' variables with valid login credentials.
    4. Having at least one quiz for review
    
The script consists of the following functions:
    - login(driver): Logs into the web application.
    - goto_reviewquiz(driver): Goes to the review quiz tab.
    - test_buttons(): Test all of the buttons needed testing in the review quiz tab.
    
Script Execution:
    When executed, the script performs the following steps:
    1. Opens a Chrome browser using the WebDriver.
    2. Logs in to the web application using the provided credentials.
    3. Tests the "Review Quiz" functionality and it's buttons.
    4. Prints a success message if the test is successful; otherwise, it prints a failure message.
    5. Properly closes the WebDriver.
"""

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

# change credentials to an existing user that has a review to do
username = "justAUser1"
password = "admin123"


def login(driver):
    """LOGIN

    Logs into the web application.

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Raises:
        Exception: If the login page cannot be loaded

    Returns:
        _type_: None
    """
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    login_button.click()
    return True


def goto_reviewquiz(driver):
    """
    Goes the "Review quiz" tab of the web application.

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Returns:
        bool: True if the tab is successful; False otherwise
    """
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "links_nav")))
    create_quiz_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[3]/a/b")
    create_quiz_button.click()

    expected_url = "http://localhost:3000/review-quizz"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Review Quiz button")
        return False

    return True


def test_buttons():
    """
    Tests all of the buttons in the review quiz tab that need testing (Cancel and Logo).

    Args:

    Returns:
        bool: True if the test is successful; False otherwise
    """
    driver = webdriver.Chrome()
    # Use of an implicit wait (5 seconds) in case an element is not immeadiately found
    driver.implicitly_wait(5)

    login(driver)
    goto_reviewquiz(driver)

    driver.maximize_window()

    # TEST LOGO BUTTON
    # Easy way to find buttons

    logo_button = driver.find_element(By.ID, 'logo_return_home')
    expectedUrl_logoButton = "http://localhost:3000/"

    logo_button.click()

    actualUrl = driver.current_url

    if actualUrl != expectedUrl_logoButton:
        print("Expected a different redirection from LOGO button")
        return False

    driver.back()

    cancel_button = driver.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/div/button[2]')
    expectedUrl_cancelButton = "http://localhost:3000/"
    cancel_button.click()
    actualUrl = driver.current_url
    if expectedUrl_cancelButton != actualUrl:
        print("Expected a different redirection from Cancel button")
        return False
    driver.back()

    print("TEST SUCESSUFUL! ALL BUTTONS WORKING")
    driver.close()
    return True


if __name__ == "__main__":
    if test_buttons() == True:
        print("Test4.1_buttons.py is a SUCESS")
    else:
        print("Test4.1_buttons.py failed :(")
