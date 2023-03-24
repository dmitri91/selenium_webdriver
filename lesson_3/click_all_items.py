import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/admin/")
    wd.find_element(By.NAME, "username").send_keys("admin")
    wd.find_element(By.NAME, "password").send_keys("admin")
    wd.find_element(By.NAME, "login").click()
    yield wd
    wd.quit()


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


def test_click_all_items(driver):
    for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app-"))):
        blocks = driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app-")
        blocks[i].click()
        blocks = driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app-")
        if are_elements_present(blocks[i], By.CSS_SELECTOR, 'li'):
            for j in range(1, len(driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app- li"))+1):
                driver.find_element(By.CSS_SELECTOR, f"#box-apps-menu #app- li:nth-child({j})").click()
