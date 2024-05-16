import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables
load_dotenv()

# Retrieve secrets from environment variables
secret_recovery_phrase = os.getenv('SECRET_RECOVERY_PHRASE')
password = os.getenv('PASSWORD')


def enter_secret_recovery_phrase(driver, recovery_phrase):
    words = recovery_phrase.split()
    for i, word in enumerate(words):
        input_xpath = f"//input[@id='import-srp__srp-word-{i}']"
        word_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, input_xpath))
        )
        word_input.clear()  # Clear any pre-existing text
        word_input.send_keys(word)  # Input the word into the field


def get_ethereum_address(driver):
    address_xpath = "//div[@class='mm-box mm-box--display-flex']"
    address_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, address_xpath))
    )
    return address_element.text




#download chromedriver
driver_path = ChromeDriverManager().install()

# Path to the MetaMask extension
extension_path = 'MetaMask 11.15.4.0.crx'  # Adjust the path accordingly
options = webdriver.ChromeOptions()
options.add_extension(extension_path)

# Initialize the WebDriver
service = ChromeService(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open MetaMask extension page
extension_page = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password'
driver.get(extension_page)
time.sleep(5)  # Adjust sleep time

# Switch to MetaMask extension
driver.switch_to.window(driver.window_handles[0])

# Wait for and click
agree_terms_checkbox = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#onboarding__terms-checkbox")))
agree_terms_checkbox.click()
time.sleep(2)

#Import existing wallet
wallet = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class ='button btn--rounded btn-secondary']")))
wallet.click()
time.sleep(2)

#aclick on i agree button
agree_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class ='button btn--rounded btn-primary btn--large']")))
agree_button.click()
time.sleep(2)

enter_secret_recovery_phrase(driver, secret_recovery_phrase)

#click on the confirm secret phrase

confirm_secret = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class ='button btn--rounded btn-primary btn--large import-srp__confirm-button']")))
confirm_secret.click()
time.sleep(3)
#click on entering the password

create_password = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@class ='form-field__input']")))
create_password.click()
create_password.clear()
create_password.send_keys("password")
time.sleep(3)

#confirm password

confirm_password = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='create-password-confirm']")))
confirm_password.click()
confirm_password.clear()
confirm_password.send_keys("password")
time.sleep(3)

#click on the check box

checkbox_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@class ='check-box far fa-square']")))
checkbox_button.click()
time.sleep(3)

#import my wallet
import_wallet = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class ='button btn--rounded btn-primary btn--large create-password__form--submit-button']")))
import_wallet.click()
time.sleep(3)

#click got it button
got_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class ='button btn--rounded btn-primary btn--large']")))
got_button.click()
time.sleep(2)

#next button
next_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class ='button btn--rounded btn-primary']")))
next_button.click()
time.sleep(2)

#done button
done_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class ='button btn--rounded btn-primary']")))
done_button.click()
time.sleep(2)

NoThanks_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text() ='No thanks']")))
NoThanks_button.click()
time.sleep(2)


threedot_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class ='mm-box mm-icon mm-icon--size-sm mm-box--display-inline-block mm-box--color-inherit']")))
threedot_button.click()
time.sleep(2)

Accounts_details = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text() ='Account details']")))
Accounts_details.click()
time.sleep(2)

# Retrieve and print Ethereum address
ethereum_address = get_ethereum_address(driver)
print("Ethereum Address:", ethereum_address)


driver.quit()


