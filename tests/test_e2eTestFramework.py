import json
import os.path
import sys
import os
import pytest
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.checkout_confirmation import Checkout_Confirmation
from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage

from pathlib import Path
from utils.browserutils import TestBrowserUtils





test_data_path = '../data/test_e2eTestFramework.json'

#print("Looking for file at:", test_data_path)
#test_data_path = '../data/test_e2eTestFramework.json'
#test_data_path = "/Users/scottjones/PycharmProjects/PythonTesting/pytestsE2eFramework2/data/test_e2eTestFramework.json"
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_e2eTestFramework.json')
file_path = os.path.abspath(file_path)

with open(file_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]



@pytest.mark.smoke
@pytest.mark.full
@pytest.mark.parametrize("test_list_item", test_list)


def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address(test_list_item["countryOption"], test_list_item["countryName"])
    checkout_confirmation.validate_order()
    print(checkout_confirmation.getTitle())






