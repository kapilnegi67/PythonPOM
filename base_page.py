'''
Created on 17-Apr-2021

@author: kapilnegi
'''

from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    admin_tab = (By.ID, "menu_admin_viewAdminModule")
    pim_tab = (By.ID, "menu_pim_viewPimModule")
    welcome_btn = (By.ID, "welcome")
    logout_btn = (By.LINK_TEXT, "Logout")

    def go_to_admin_tab(self):
        self.driver.find_element(self.admin_tab).click()

    def go_to_pim_tab(self):
        self.driver.find_element(self.pim_tab).click()

    def logout(self):
        self.driver.find_element(self.welcome_btn).click()
        self.driver.find_element(self.logout_btn).click()