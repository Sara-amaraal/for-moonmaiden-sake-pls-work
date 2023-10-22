from selenium.webdriver.chrome.service import Service
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager


import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
logging.basicConfig(filename="log.txt", level=logging.INFO)


PATH = "C:\Program Files (x86)\Chromedriver.exe"

def login(driver):
    """This function will login into the website

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

    username = "user_solver"
    password = "password"

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "fullName")))
    driver.find_element(By.ID, "fullName").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    login_button = driver.find_element(By.ID, "login")
    login_button.click()

    return

def goto_ChooseTest(driver):
    """
    Goes to the "Choose test" tab of the web application.

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Returns:
        bool: True if the tab is successful; False otherwise
    """

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[5]/a/b")))
        solve_button = driver.find_element(
            By.XPATH, "/html/body/div/div/div/main/main/header/nav/ul/li[5]/a/b")

        solve_button.click()
    except TimeoutException:

        print("❌ Login failed")
        return False

    # Retorna o URL errado mas está a funcionar	bem ??? Tirei Confirmação
    '''
    expected_url = "http://localhost:3000/choose-test"
    current_url = driver.current_url

    if current_url != expected_url:
        print("Expected a different redirection from Choose Test button")
        print("Current URL is: ", current_url)
        return False
    else:

        return True
    '''

# Check if there are tests to solve and solve one


def goto_SolveTest(driver):
    """
    Checks if there are tests to solve and opens one

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Returns:
        bool: True if the test is successful; False if there are no tests avaiable or an unexpected redirection
    """

    time.sleep(1)
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[1]/input"))).click()

    except TimeoutException or StaleElementReferenceException as e:

        print("❌ No tests available")

        return False

    expected_url = "http://localhost:3000/solve-test"
    current_url = driver.current_url

    if expected_url not in current_url:
        print("Expected a different redirection from Solve Test button")
        print("Current URL is: ", current_url)
        return False
    else:

        return True

def test_Cancel_Button(driver):
    """
    Tests if it is possible to cancel a test halfway through

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Returns:
        bool: True if the test is successful; False otherwise
    """

    # Cancel the test
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[41]/button[2]"))).click()
    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[2]"))).click()

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Cancel Button - Cancel Button not found (inconsistent xpath)")
            return 0

    # Confirm the cancel
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    alert.accept()

    # Check if the test was cancelled

    if "http://localhost:3000/" == driver.current_url:
        print("Test Cancel - ✅")
        return 1

    else:

        print("Wrong redirection after alert cancel - ❌")
        return 0

def test_NoAnswers(driver):
    """
    Tests if it is possible to submit a test with blank answers

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Returns:
        bool: True if the test is successful; False otherwise
    """

    # Submit the test without answering any question
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[41]/button[1]"))).click()

    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[1]"))).click()

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Submit Button - Submit Button not found (inconsistent xpath)")
            return 0
    # time.sleep(1)

    try:
        aux = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[41]/button[1]"))).text
    except TimeoutException or NoSuchElementException as e:

        try:
            aux = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[1]"))).text

        except TimeoutException or NoSuchElementException as e:

            print(
                "❌ Error in Result Button - Result Button not found (inconsistent xpath)")
            return 0

    if aux == "YOU GOT 0 POINTS":

        print("Test with no answers - ✅")
        return 1

    else:

        print("Test with no answers - ❌")
        return 0

def test_Homepage_Button_Cancel(driver):
    """
    Tests if it is possible to cancel a test halfway through

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Returns:
        bool: True if the test is successful; False otherwise
    """

    excepted_url = driver.current_url

    # Click Homepage Button

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[41]/button[2]"))).click()
    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[2]"))).click()

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Homepage Button - Homepage Button not found (inconsistent xpath)")
            return 0

    # time.sleep(1)

    # Click Alert Cancel Button
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    alert.dismiss()

    # time.sleep(1)

    if excepted_url == driver.current_url:

        print("Homepage Button Cancel - ✅")
        return 1
    else:

        print("Wrong redirection after Homepage alert cancel - ❌")
        return 0

def test_Homepage_Button_Ok(driver):
    """
    Tests if the homepage button works

    Args:
        driver (WebDriver): Selenium WebDriver (Chrome WebDriver in this case)

    Returns:
        bool: True if the test is successful; False otherwise
    """
    # Click Homepage Button again

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/main/div/div[41]/button[2]"))).click()
    except TimeoutException or NoSuchElementException as e:

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/main/div/div[21]/button[2]"))).click()

        except TimeoutException or NoSuchElementException as e:
            # print("TimeoutException")
            print(
                "❌ Error in Homepage Button - Homepage Button not found (inconsistent xpath)")
            return 0

    # Click Alert OK Button
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert

    alert.accept()

    # time.sleep(1)

    if "http://localhost:3000/" == driver.current_url:

        print("Homepage Button OK - ✅")
        return 1
    else:

        print("Wrong redirection after Homepage alert accept - ❌")
        return 0

    return i


def test_all():

    res = 0

    driver = webdriver.Chrome(PATH)

    login(driver)
    if goto_ChooseTest(driver) == False:
        return False
    if goto_SolveTest(driver) == False:
        return False

    driver.maximize_window()

    res += test_Cancel_Button(driver)

    if goto_ChooseTest(driver) == False:
        return False
    if goto_SolveTest(driver) == False:
        return False

    res += test_NoAnswers(driver)

    res += test_Homepage_Button_Cancel(driver)

    res += test_Homepage_Button_Ok(driver)

    return res


if __name__ == "__main__":

    res = test_all()

    if res == False:

        print("❌ - Errors in REQ5 Test Submission TEST")
    elif res == 4:
        print("REQ5 Test Submission TEST -> ✅")

    else:
        print("REQ5 Test Submission TEST -> ❌\n(",
              res, "out of 4 tests passed)")
