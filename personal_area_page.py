import unittest
import Driver_setup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import elik_login

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Driver_setup.mydriver("https://qa.trado.cp.il/app")
elik_login.log_in()

class Unittest(unittest.TestCase):
    def test_delivery_details(self):

        edit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'form_editModeSubmitBtn ')))
        edit.click()

        first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[1]/span/input'))).click()
        first_name.send_keys("Moshe")

        last_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[2]/span/input'))).click()
        last_name.send_keys("Aharon")

        email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[4]/span/input')))).click()
        email.send_keys("moshe123@gmail.com")

    def test_business_details(self):

        city_and_street = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[1]/input'))).click()
        city_and_street.send_keys("city/st")

        street_num = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[2]/input'))).click()
        street_num.send_keys("8")

        zip_code = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[3]/input'))).click()
        zip_code.send_keys("81234132")

    def test_my_wallet(self):

        withdraw_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'button_button userWallet_eTrado_btn')))
        withdraw_btn.click()

    def test_contact_us_navigation(self):

        contact_us_btns = ['//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/span/a/label',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[4]/div[3]/span/a/label',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/span/a/label',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/span/a/label']

        for btn in contact_us_btns:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn))).click()









