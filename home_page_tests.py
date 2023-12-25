import unittest
import Driver_setup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Driver_setup.mydriver("https://qa.trado.ai")

class Unittest(unittest.TestCase):



    def test_logo(self):
        """
        Testing app's logo's functionality.
        :return:
        """
        click_logo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[2]/a/div/a/img")))
        click_logo.click()

    def test_search_engine(self):
        """
        Testing apps search engine.
        :return:
        """
        click_search_engine = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[2]/div")))
        click_search_logo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[2]/div/div[2]")))
        click_search_engine.click()
        click_search_engine.send_keys("sldkjfm")
        click_search_logo.click()

    def test_go_to_personal_area(self):
        """
        Testing navigation to personal area.
        :return:
        """
        go_to_pa = WebDriverWait(driver, 10).until((EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/header/div/div/div[1]/a"))))
        go_to_pa.click()

    def test_go_to_item_categories(self):
        """
        Testing navigation to item categories.
        In order to navigate to the item categories page you need to press an item and not a button to lead you there.
        :return:
        """
        item_categories = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[1]/div/a/div',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[2]/div/a/div',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[3]/div/a/div',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[4]/div/a/div',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[5]/div/a/div',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[6]/div/a/div',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[7]/div/a/div',
                           '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[8]/div/a/div']

        for item in item_categories:
            click_items = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, item)))
            click_items.click()

    def test_go_to_item_upload(self):
        """
        Testing navigation to item upload
        :return:
        """
        go_to_item_upload = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/div[1]/button')))
        go_to_item_upload.click()

    def test_switch_lang(self):
        """
        Testing switching language feature
        :return:
        """
        switch_lang = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]')))
        switch_lang.click()

    def test_go_to_accessibility(self):
        """
        testing navigation to accessibility page
        :return:
        """
        go_to_accessibility = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="enable-toolbar-trigger-svg"]/circle[1]')))
        go_to_accessibility.click()

    def test_footer(self):
        """
        Testing navigation through footer links
        :return:
        """
        footer_links = ['//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[1]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[2]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[3]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[4]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[1]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[2]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[3]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[4]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[1]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[2]',
                        '//*[@id="root"]/div/div[2]/div[3]/div/div[5]/div/a[3]'
                        ]

        for link in footer_links:
            footer_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
            footer_click.click()

    def test_logout(self):
        """
        Testing Logout functionality
        :return:
        """
        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/header/div/div/a/span')))
        logout_btn.click()

