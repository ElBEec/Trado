import time
import unittest
import Driver_set_up_&_Log_in
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Driver_setup.mydriver("https://qa.trado.cp.il/app")

class Unittest(unittest.TestCase):

    def test_sign_in(self):
        """
        Testing Sign in functionality
        :return:
        """

        #Testing sign in with Facebook API
        sign_in_with_fb = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login_facebook metro')))
        sign_in_with_fb.click()
        time.sleep(5)

        # Testing sign in with Google API
        sign_in_with_google = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login_google')))
        sign_in_with_google.click()
        time.sleep(5)

        # Testing sign in with Twitter API
        sign_in_with_twitter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login_twitter')))
        sign_in_with_twitter.click()
        time.sleep(5)

        sign_in_phone = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'form-control ')))
        sign_in_phone.send_keys(Driver_setup.phone)
        time.sleep(5)

        id_num = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input')))
        id_num.send_keys("123456")
        time.sleep(5)

        accept_user_registration_agreement = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.CLASS_NAME, 'micon-check icon_icon '))))
        accept_user_registration_agreement.click()

        enterance_btn = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.CLASS_NAME, 'form_submitBtn'))))
        enterance_btn.click()






