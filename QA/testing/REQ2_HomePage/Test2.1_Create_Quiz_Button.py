"""
Automated Testing Script for 'Create_Quiz' functionality of the Web Application using the Selenium library

Usage:
    1. Having Selenium installed.
    2. Provide an appropriate Chrome WebDriver executable (chromedriver.exe) in the PATH.
    3. Set the 'username' and 'password' variables with valid login credentials.

The script consists of the following functions:
    - login(driver, username, password): Logs into the web application.
    - test_create_quiz(driver): Tests the "Create Quiz" functionality.
    
Script Execution:
    When executed, the script performs the following steps:
    1. Opens a Chrome browser using the WebDriver.
    2. Logs in to the web application using the provided credentials.
    3. Tests the "Create Quiz" functionality.
    4. Prints a success message if the test is successful; otherwise, it prints a failure message.
    5. Properly closes the WebDriver.

"""

import sys
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename="log.txt", level=logging.INFO)


def login(driver, username, password):
    """
    Logs into the web application.

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)
        username (str): username for the login
        password (str): password for the login

    Raises:
        Exception: If the login page cannot be loaded (#1) or if there are errors during the login process (#2)

    Returns:
        _type_: None
    """
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception("Unable to load Login Page")  # 1

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "fullName"))
        )
    except Exception as e:
        logging.error(f"Error waiting for login page: {e}")
        raise  # 2

    driver.maximize_window()

    # Removed hardcoded username and password which allows passing different credentials when calling the function
    try:
        username_input = driver.find_element(By.ID, "fullName")
        password_input = driver.find_element(By.ID, "pass")
        login_button = driver.find_element(By.ID, "login")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    except Exception as e:
        logging.error(f"Error logging in: {e}")
        raise


def test_create_quiz(driver):
    """
    Tests the "Create Quiz" functionality of the web application.
    Result must be being redirected to the 'expected_link'.

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Raises:
        Exception: If any errors are faced during the testing process

    Returns:
        bool: True if the test is successful; False otherwise
    """
    driver.get("http://localhost:3000/create-quizz")

    try:
        WebDriverWait(driver, 5).until(
            EC.url_matches("http://localhost:3000/create-quizz")
        )

        create_quiz_button = driver.find_element(
            By.XPATH, '//*[@id="links_nav"]/li[2]/a/b'
        )

        create_quiz_button.click()

        expected_url = "http://localhost:3000/create-quizz"
        current_url = driver.current_url

        if current_url == expected_url:
            return True

    except Exception as e:
        logging.error(f"Error testing Create Quiz: {e}")
        return False


if __name__ == "__main__":
    username = "justAUser1"
    password = "admin123"

    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(
            5
        )  # Use of an implicit wait (5 seconds) in case an element is not immeadiately found

        login(driver, username, password)

        if test_create_quiz(driver):
            print("Test2.1_Create_Quiz_Button.py is a SUCCESS")
        else:
            print("Test2.1_Create_Quiz_Button.py failed :(")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if driver:
            driver.quit()  # Quit the WebDriver to clean up resources and close correctly
