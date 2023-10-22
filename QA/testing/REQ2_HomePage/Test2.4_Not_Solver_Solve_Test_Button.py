"""
Automated Testing Script for 'Solve Test' Functionality for Non-Solvers of the Web Application using the Selenium library

Usage:
    1. Having Selenium installed.
    2. Provide an appropriate Chrome WebDriver executable (chromedriver.exe) in the PATH.
    3. Set the 'username' and 'password' variables with valid login credentials.

The script consists of the following functions:
    - login(driver): Logs into the web application as a Non-Solver.
    - test_solve_test(driver): Tests the "Solve Test" functionality for Non-Solvers.

Script Execution:
    When executed, the script performs the following steps:
    1. Opens a Chrome browser using the WebDriver.
    2. Logs in as a Non-Solver to the web application using the provided credentials.
    3. Tests the "Solve Test" functionality.
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

    # Não existe na Database, basta registar um novo user num server local ou na VM do DEI e usar essas credenciais aqui para correr o test
    username = "creator1"
    password = "password"

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return


def test_solve_test(driver):
    """
    Tests the "Solve Test" functionality for Non-Solvers.
    Result must be being redirected to the 'expected_link'.

    Args:
        driver (WebDriver): Selenium WebDriver

    Returns:
        int: 2 if the test is successful, 0 otherwise
    """
    i = 0
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="links_nav"]/li[5]/a/b'))
    )

    solve_button = driver.find_element(By.XPATH, '//*[@id="links_nav"]/li[5]/a/b')

    solve_button.click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    msg = alert.text

    if msg == "Must be a Solver":
        i += 1

    alert.accept()

    expected_url = "http://localhost:3000/"
    current_url = driver.current_url

    if current_url == expected_url:
        i += 1

    return i


PATH = "C:\Program Files (x86)\Chromedriver.exe"

if __name__ == "__main__":
    driver = webdriver.Chrome(PATH)

    login(driver)

    if test_solve_test(driver) == 2:
        print("Test2.4_Not_Solver_Solve_Test_Button.py is a SUCESS")
    else:
        print("Test2.4_Not_Solver_Solve_Test_Button.py failed :(")

    driver.close()
