import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("http://localhost/litecart/en/")
    yield wd
    wd.quit()


def test_user_registration(driver):
    base_part = "n_novgorod"
    domain = "example.com"
    random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    email = f"{base_part}{random_part}@{domain}"
    tax_id = "123-456-789"
    company = "nn_live"
    first_name = "Dmitry"
    last_name = "Ivanov"
    address_1 = "Н.Новгород, ул. Школьная, д.30"
    postcode = "607800"
    city = "N Novgorod"
    country = "Russian Federation"
    phone = "+79290332211"
    password = "123qwa"
    driver.find_element(By.CSS_SELECTOR, ".content tbody>tr:last-child").click()
    driver.find_element(By.CSS_SELECTOR, 'td [name="tax_id"]').send_keys(tax_id)
    driver.find_element(By.CSS_SELECTOR, 'td [name="company"]').send_keys(company)
    driver.find_element(By.CSS_SELECTOR,'td [name="firstname"]').send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR, 'td [name="lastname"]').send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, 'td [name="address1"]').send_keys(address_1)
    driver.find_element(By.CSS_SELECTOR, 'td [name="postcode"]').send_keys(postcode)
    driver.find_element(By.CSS_SELECTOR, 'td [name="city"]').send_keys(city)
    driver.find_element(By.CSS_SELECTOR, '[class*="select2-selection--single"]').click()
    driver.find_element(By.CSS_SELECTOR, '.select2-search__field').send_keys(country)
    driver.find_element(By.XPATH, f"//li[contains(text(), '{country}')]").click()
    driver.find_element(By.CSS_SELECTOR, 'td [name="email"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, 'td [name="phone"]').send_keys(phone)
    driver.find_element(By.CSS_SELECTOR, 'td [name="password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'td [name="confirmed_password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'td [name="create_account"]').click()
    driver.find_element(By.CSS_SELECTOR, '#box-account li:last-child a').click()
    driver.find_element(By.CSS_SELECTOR, 'td [name="email"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, 'td [name="password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'td [name="login"]').click()
    driver.find_element(By.CSS_SELECTOR, '#box-account li:last-child a').click()





