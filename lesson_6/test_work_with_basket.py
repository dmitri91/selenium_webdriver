import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/en/")
    yield wd
    wd.quit()


def test_delete_duck_from_basket(driver):
    wait = WebDriverWait(driver, 10)
    for i in range(1, 4):
        driver.find_element(By.CSS_SELECTOR, '.listing-wrapper a').click()
        driver.find_element(By.CSS_SELECTOR, '[name="add_cart_product"]').click()
        wait.until(EC.presence_of_element_located((By.XPATH, f"//*[@class='quantity'][contains(text(),'{i}')]")))
        driver.find_element(By.CSS_SELECTOR, '.general-0 a').click()
    driver.find_element(By.CSS_SELECTOR, '#cart .link').click()
    elements = driver.find_elements(By.CSS_SELECTOR, '.dataTable .item')
    for _ in range(1, len(elements)):
        data_table = driver.find_element(By.CSS_SELECTOR, '#box-checkout-summary tbody')
        driver.find_element(By.CSS_SELECTOR, '[name="remove_cart_item"]').click()
        wait.until(EC.staleness_of(data_table))
