import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    # wd.implicitly_wait(4)
    wd.get("http://localhost/litecart/admin/")
    wd.find_element(By.NAME, "username").send_keys("admin")
    wd.find_element(By.NAME, "password").send_keys("admin")
    wd.find_element(By.NAME, "login").click()
    yield wd
    wd.quit()


def open_directory(driver):
    lens = len(driver.find_elements(By.CSS_SELECTOR, '.fa-folder + a'))
    while lens != 0:
        driver.find_element(By.CSS_SELECTOR, ".fa-folder + a").click()
        lens = len(driver.find_elements(By.CSS_SELECTOR, '.fa-folder + a'))

def test_message_in_browser(driver):
    driver.find_element(By.XPATH, "//*[contains(text(),'Catalog')]").click()
    open_directory(driver)
    for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)>a'))):
        if i != 0:
            open_directory(driver)
        ducks = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(3)>a")
        ducks[i].click()
        assert len(driver.get_log("browser")) == 0, "Ошибка в браузере при открытии товавра в каталоге"
        driver.find_element(By.CSS_SELECTOR, '[id="doc-catalog"]').click()
