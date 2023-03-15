import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/admin/")
    yield wd
    wd.quit()


def test_login(driver):
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()
