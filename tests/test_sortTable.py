import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#Chrome Driver Service

@pytest.mark.full
def test_sort(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.implicitly_wait(2)  # 2 seconds is max timeout; applied globally for script to apply to all checks / processes
    browserSortedVeggies = []

    # Click on Column Header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    # Collect all Veggie Names
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for veggieWebElement in veggieWebElements:
        browserSortedVeggies.append(veggieWebElement.text)

    originalBrowserSortedVeggies = browserSortedVeggies.copy()  # use copy method when creating a copy of a list
    print(originalBrowserSortedVeggies)

    # Sort Veggie List
    browserSortedVeggies.sort()
    print(browserSortedVeggies)
    assert browserSortedVeggies == originalBrowserSortedVeggies

    time.sleep(2)