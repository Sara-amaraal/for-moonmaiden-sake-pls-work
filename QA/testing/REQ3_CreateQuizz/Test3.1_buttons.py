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


def test_buttons():
    """This function will test if all the buttons are correct. If all buttons work it will return true. False otherwise.

    Args:

    Returns:
        True if all the buttons worked, False otherwise.

    """
    """Next, create an instance of Chrome with the path of the driver that you downloaded through the websites of the respective browser.
    In this example, we assume that the driver is in the same directory as the Python script that you will execute."""
    driver = webdriver.Chrome(ChromeDriverManager().install(
    ))  # or driver = webdriver.Chrome('./chromedriver')
    login(driver)
    goto_createQuiz(driver)

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

    save_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div/div/div[5]/div/div[2]/a/input")
    expectedUrl_saveButton = "http://localhost:3000/"

    save_button.click()
    actualUrl = driver.current_url
    if actualUrl != expectedUrl_saveButton:
        print("Expected a different redirection from SAVE button")
        return False
    driver.back()

    cancel_button = driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div[5]/div/div[1]/a/input')
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
        print("Test3.1_buttons.py is a SUCESS")
    else:
        print("Test3.1_buttons.py failed :(")
