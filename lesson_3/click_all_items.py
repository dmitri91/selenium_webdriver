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


def test_login(driver):
    driver.find_element(By.CSS_SELECTOR, '[href*="appearance"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-logotype').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '[href*="catalog"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-product_groups').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-option_groups').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-manufacturers').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-suppliers').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-delivery_statuses').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-sold_out_statuses').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-quantity_units').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-csv').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # countries
    driver.find_element(By.CSS_SELECTOR, '[href*="countries"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # customers
    driver.find_element(By.CSS_SELECTOR, '[href*="customers"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-csv').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-newsletter').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # geo_zones
    driver.find_element(By.CSS_SELECTOR, '[href*="geo_zones"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # languages
    driver.find_element(By.CSS_SELECTOR, '[href*="languages"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-storage_encoding').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # modules
    driver.find_element(By.CSS_SELECTOR, '[href*="modules"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-customer').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-shipping').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-payment').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-order_total').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-order_success').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-order_action').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # orders
    driver.find_element(By.CSS_SELECTOR, 'a[href*="orders"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-order_statuses').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # pages
    driver.find_element(By.CSS_SELECTOR, 'a[href*="pages"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # reports
    driver.find_element(By.CSS_SELECTOR, 'a[href*="reports"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-most_sold_products').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-most_shopping_customers').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # reports
    driver.find_element(By.CSS_SELECTOR, 'a[href*="store_info"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-defaults').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-general').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-listings').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-images').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-checkout').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-advanced').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-security').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # slides
    driver.find_element(By.CSS_SELECTOR, 'a[href*="slides"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # tax
    driver.find_element(By.CSS_SELECTOR, 'a[href*="tax"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-tax_rates').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # tax
    driver.find_element(By.CSS_SELECTOR, 'a[href*="translations"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-scan').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    driver.find_element(By.CSS_SELECTOR, '#doc-csv').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # user
    driver.find_element(By.CSS_SELECTOR, 'a[href*="user"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"
    # vqmods
    driver.find_element(By.CSS_SELECTOR, 'a[href*="vqmods"]').click()
    assert are_elements_present(driver, By.CSS_SELECTOR, 'h1 [class*="icon-wrapper"]'), "Не найден заголовок"




