import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import Select
from datetime import date, timedelta


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    wd.find_element(By.NAME, "username").send_keys("admin")
    wd.find_element(By.NAME, "password").send_keys("admin")
    wd.find_element(By.NAME, "login").click()
    yield wd
    wd.quit()


def test_add_product(driver):
    name_p = "super duck"
    code = "duck_12"
    start_date = date.today().strftime("%d-%m-%Y")
    end_date = (date.today() + timedelta(days=7)).strftime("%d-%m-%Y")
    driver.find_element(By.CSS_SELECTOR, "#content div>a:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, '[type="radio"][value="1"]').click()
    driver.find_element(By.CSS_SELECTOR, '[name*="name"]').send_keys(name_p)
    driver.find_element(By.CSS_SELECTOR, '[name="code"]').send_keys(code)
    driver.find_element(By.CSS_SELECTOR, '[value="1-2"]').click()
    driver.find_element(By.CSS_SELECTOR, '[name="quantity"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[name="quantity"]').send_keys("10")
    driver.find_element(By.CSS_SELECTOR, '[name*="new_images"]').send_keys(os.getcwd()+"/duck.png")

    driver.find_element(By.CSS_SELECTOR, '[name="date_valid_from"]').send_keys(start_date)
    driver.find_element(By.CSS_SELECTOR, '[name="date_valid_to"]').send_keys(end_date)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Information')]").click()
    select_man = Select(driver.find_element(By.CSS_SELECTOR, '[name="manufacturer_id"]'))
    select_man.select_by_value("1")
    driver.find_element(By.CSS_SELECTOR, '[name="keywords"]').send_keys("keyWords")
    driver.find_element(By.CSS_SELECTOR, '[name*="short_description"]').send_keys("Short Description")
    driver.find_element(By.CSS_SELECTOR, '[class="trumbowyg-editor"]').send_keys("Long Description")
    driver.find_element(By.CSS_SELECTOR, '[name*="head_title"]').send_keys("head_title")
    driver.find_element(By.CSS_SELECTOR, '[name*="meta_description"]').send_keys("meta_description")

    driver.find_element(By.XPATH, "//a[contains(text(), 'Prices')]").click()
    driver.find_element(By.CSS_SELECTOR, '[name="purchase_price"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[name="purchase_price"]').send_keys("12")
    select_man = Select(driver.find_element(By.CSS_SELECTOR, '[name="purchase_price_currency_code"]'))
    select_man.select_by_value("USD")
    driver.find_element(By.CSS_SELECTOR, '[name="prices[USD]"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[name="prices[USD]"]').send_keys("66")
    driver.find_element(By.CSS_SELECTOR, '[name="prices[EUR]"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[name="prices[EUR]"]').send_keys("77")
    driver.find_element(By.CSS_SELECTOR, '[name="save"]').click()
    assert driver.find_elements(By.XPATH, f"//a[contains(text(), '{name_p}')]") != [], "Товар не добавлен"
