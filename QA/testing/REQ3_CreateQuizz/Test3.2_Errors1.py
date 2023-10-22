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


"""
INFO ABOUT THE BOXES
Quizz Structure:

1. Question: 20 - 140
2. Description: 0 - 512
3. 6 Options: only 1 is Correct

Question box with a mark box (to the correct one)
Only one mark box can be selected (when user selects: unmark the other)
'Submit', 'Save' and 'Cancel' button

"""


def get_random_string(length):
    """This function will create a random string. It will return a string.

    Args:
        lenght: Size of the string to be created.

    Returns:
        A string of random letters.

    """
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters)
                         for i in range(length))
    # print random string
    return result_str


def login(driver):
    """This function will login into the website. It will return True if the login was successful, False otherwise.

    Args:
        driver: The webdriver that is being used.

    Returns:
        True if the login was successful, False otherwise.

    """
    driver.get("http://localhost:3000/login")

    if not "Login Page" in driver.title:
        raise Exception("Unable to load Login Page")

    driver.maximize_window()

    username = "creator1"
    password = "password"

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()
    login_button.click()
    return True


def goto_createQuiz(driver):
    """This function will go to createQuizz. It will return True if it was redirected to create-quizz. False otherwise.

    Args:
        driver: The webdriver that is being used.

    Returns:
        True if the redirect was successful, False otherwise.

    """
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "links_nav")))
    create_quiz_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[2]/a/b")
    create_quiz_button.click()

    expected_url = "http://localhost:3000/create-quizz"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Create Quiz button")
        return False

    return True


def test_errors1():
    """This function test if the program detects empty input boxes. Returns true if it is detected. False otherwise (url changes).

    Args:

    Raises:
        Exception: If the login page cannot be loaded

    Returns:
        True if empty input boxes are detected, False otherwise.

    """
    # TEST FOR INPUT BOXES
    # or driver = webdriver.Chrome('./chromedriver')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    login(driver)
    goto_createQuiz(driver)

    driver.maximize_window()

    # TEST FOR EMPTY INPUT BOXES, SHOULDN'T WORK
    submit_button = driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div[5]/div/div[3]/input')
    submit_button.click()
    try:

        WebDriverWait(driver, 1).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print("Alert accepted")
        expectedUrl = "http://localhost:3000/create-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
            return False
    except TimeoutException:
        print("No alert")
        expectedUrl = "http://localhost:3000/create-quizz"
        if driver.current_url != expectedUrl:
            print("ERROR: Page CHANGED")
        return False

    # SHOULDN'T CHANGE PAGE!
    expectedUrl = "http://localhost:3000/create-quizz"
    if driver.current_url != expectedUrl:
        print("ERROR: Page CHANGED")
        return False

    driver.close()
    return True


if __name__ == "__main__":
    if test_errors1() == True:
        print("Test3.2_Errors1.py is a SUCESS")
    else:
        print("Test3.2_Errors1.py failed :(")
