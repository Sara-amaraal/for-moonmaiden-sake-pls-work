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

    Raises:
        Exception: If the login page cannot be loaded

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


def test_submit():
    """This function test the submission of a new quiz. Returns true a new quiz is submitted. False otherwise (different url).

    Args:

    Returns:
        True if new quiz is submitted, False otherwise.

    """

    # TEST FOR INPUT BOXES
    # or driver = webdriver.Chrome('./chromedriver')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    login(driver)
    goto_createQuiz(driver)

    driver.maximize_window()

    inputboxes = driver.find_elements(By.ID, 'option')

    # Write in all boxes
    for box in inputboxes:
        # Fill up with more than MAX (ERROR SHOULD APPEAR WHEN SUBMITING)
        box.send_keys(get_random_string(5))
    justification_box = driver.find_element(By.NAME, 'justification')
    justification_box.send_keys(get_random_string(10))
    submit_button = driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div[5]/div/div[3]/input')
    question_box = driver.find_element(By.ID, 'question')
    question_box.send_keys(get_random_string(10))
    check_button = driver.find_element(By.ID, "check")
    check_button.click()
    submit_button = driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div[5]/div/div[3]/input')
    submit_button.click()

    expectedUrl_submitButton = "http://localhost:3000/create-quizz"
    if expectedUrl_submitButton != driver.current_url:
        print("Expected a different redirection when submitting quiz")
        print(driver.current_url)
        return False
    driver.close()
    return True


if __name__ == "__main__":
    if test_submit() == True:
        print("Test3.3_Submit.py is a SUCESS")
    else:
        print("Test3.3_Submit.py failed :(")
