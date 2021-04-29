'''
Created on 17-Apr-2021

@author: kapilnegi
'''
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import sys
from os.path import abspath, dirname, join

# Update System path
sys.path.insert(0, abspath(
    join(dirname(__file__), '../../')))

from page_objects.orangeHRM.constants import URL, USERNAME, PASSWORD

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    username_txt = (By.ID, "txtUsername")
    password_txt = (By.ID, "txtPassword")
    login_btn = (By.ID, "btnLogin")
    login_panel = (By.ID, "logInPanelHeading")
    login_url = URL
    username = USERNAME
    password = PASSWORD

    # Operations
    def go_to_login_page(self):
        self.driver.get(self.login_url)

    def do_login(self):
        self.go_to_login_page()
        assert self.verify_login_page()
        self.enter_username(self.username)
        self.enter_password(self.password)
        self.click_login_btn()

    def enter_username(self, username):
        self.driver.find_element(*self.username_txt).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_txt).send_keys(password)
    
    def click_login_btn(self):
        self.driver.find_element(*self.login_btn).click()
    
    def verify_login_page(self):
        try:
            self.driver.find_element(*self.login_panel)
            return True
        except NoSuchElementException:
            return False
