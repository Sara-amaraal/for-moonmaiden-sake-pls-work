
"""
Automated Testing Script for 'Accepting Quizzes' functionality of the Web Application using the Selenium library

Usage:
    1. Having Selenium installed.
    2. Having webdriver_manager installed (pip install webdriver-manager)
    3. Set the 'username' and 'password' variables with valid login credentials.
    4. Having at least one quiz for review
    
The script consists of the following functions:
    - login(driver): Logs into the web application.
    - goto_reviewquiz(driver): Goes to the review quiz tab.
    - test_reject(): Test all of the possibilities when rejecting a quiz.
    
Script Execution:
    When executed, the script performs the following steps:
    1. Opens a Chrome browser using the WebDriver.
    2. Logs in to the web application using the provided credentials.
    3. Tests the "reject quiz" functionality and it's buttons.
    4. Prints a success message if the test is successful; otherwise, it prints a failure message.
    5. Properly closes the WebDriver.
"""
import random
import string
import sys
import logging
from typing import final
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
logging.basicConfig(filename="log.txt", level=logging.INFO)

# change credentials to an existing user that has a review to do
username = "justAUser3"
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


def get_random_string(length):
    """
    Goes to the "Review quiz" tab of the web application.

    Args:
        length (int): length of the string

    Returns:
        result_str: randomly generated string with x length
    """
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters)
                         for i in range(length))
    # print random string
    return result_str


def goto_reviewquiz(driver):
    """
    Tests the "Review quiz" tab of the web application.

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


def test_reject():
    """
    Tests the "reject" button of the "review quiz" tab of the web application.

    Args:

    Returns:
        bool: true if sucessful / false if not
    """
    driver = webdriver.Chrome()
    login(driver)
    goto_reviewquiz(driver)

    driver.maximize_window()

    # REJECT WITHOUT JUSTIFICATION
    reject_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/button[2]")
    reject_button.click()

    submit_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div/div[2]/div/button[1]")
    submit_button.click()
    try:

        WebDriverWait(driver, 1).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("Alert accepted")
        expectedUrl = "http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
            return False
    except TimeoutException:
        print("ALERT DIDN'T SHOW UP!")
        expectedUrl = "http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
        return False

    box_justificacao = driver.find_element(
        By.XPATH, "/html/body/div/div/div/div[2]/textarea")
    box_justificacao.send_keys(get_random_string(10))
    submit_button.click()

    try:

        WebDriverWait(driver, 1).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("Alert accepted")
        expectedUrl = "http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
            return False
    except TimeoutException:
        print("ALERT DIDN'T SHOW UP!")
        expectedUrl = "http://localhost:3000/review-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
        return False

    box_justificacao.send_keys(get_random_string(100))
    submit_button.click()

    expectedUrl_submitButton = "http://localhost:3000/"
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "links_nav")))  # give time for browser to load before comaparing urls

    if expectedUrl_submitButton != driver.current_url:
        print("Expected a different redirection when submitting quiz")
        print(driver.current_url)
        return False

    driver.close()
    return True


if __name__ == "__main__":
    if test_reject() == True:
        print("Test4.2_reject.py is a SUCESS")
    else:
        print("Test4.2_reject.py failed :(")
