'''
Created on 18-Apr-2021

@author: kapilnegi
'''
import pytest
from selenium import webdriver

import sys
from os.path import abspath, dirname, join

# Update System path
sys.path.insert(0, abspath(
    join(dirname(__file__), '../../../')))

from page_objects.orangeHRM.login_page import LoginPage
from page_objects.orangeHRM.admin_page import AdminPage

username_list = ["Aatmaram", "Admin", "Suresh"]


@pytest.mark.parametrize("username", username_list)
def test_search_users(username):
    driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")
    login_page_obj = LoginPage(driver)
    admin_page_obj = AdminPage(driver)

    login_page_obj.do_login()
    assert admin_page_obj.search_user(username)
    driver.quit()
