from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import logging

logger = logging.getLogger('login_tests')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')


def login_process(username, password):
    driver.get("https://www.saucedemo.com/")
    username_input = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.NAME, "user-name")))
    username_input.send_keys(username)

    password_input = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.NAME, "password")))
    password_input.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input.btn_action")))
    login_button.click()


def login_test(username, password="secret_sauce"):
    login_process(username, password)
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url


def login_error_test(error_message, username, password="secret_sauce"):
    login_process(username, password)
    error = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    assert error_message in error.text


logger.info('Starting tests...')

login_test("standard_user")
logger.info("Test 1: positive")

login_test("problem_user")
logger.info("Test 2: positive")

login_test("performance_glitch_user")
logger.info("Test 3: positive")

login_error_test("Epic sadface: Username is required", "")
logger.info("Test 4: positive")

login_error_test("Epic sadface: Password is required", "standard_user", "")
logger.info("Test 5: positive")

login_error_test("Epic sadface: Username and password do not match any user in this service", "non_existing_user")
logger.info("Test 6: positive")

login_error_test("Epic sadface: Sorry, this user has been locked out.", "locked_out_user")
logger.info("Test 7: positive")

logger.info('Tests finished.')

driver.quit()
