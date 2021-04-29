'''
Created on 17-Apr-2021

@author: kapilnegi
'''

from selenium.webdriver.common.by import By
import sys
from os.path import abspath, dirname, join

# Update System path
sys.path.insert(0, abspath(
    join(dirname(__file__), '../../')))

from page_objects.orangeHRM.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    userManagementTab = (By.ID, "menu_admin_UserManagement")
    usersTab = (By.ID, "menu_admin_viewSystemUsers")
    searchUserTxt = (By.ID, "searchSystemUser_userName")
    searchBtn = (By.ID, "searchBtn")
    searchResultUsername = (By.XPATH, "//a[contains(@href, 'saveSystemUser')]")

    def click_on_usermanagement(self):
        self.driver.find_element(*self.userManagementTab).click()

    def click_on_users_menu(self):
        self.driver.find_element(*self.usersTab).click()

    def go_to_system_userspage(self):
        self.click_on_usermanagement()
        self.click_on_users_menu()

    def search_user(self, username):
        self.driver.find_element(*self.searchUserTxt).send_keys(username)
        self.driver.find_element(*self.searchBtn).click()
        return self.driver.find_element(*self.searchResultUsername).text == username




