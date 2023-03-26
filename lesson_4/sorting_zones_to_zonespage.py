import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    wd.find_element(By.NAME, "username").send_keys("admin")
    wd.find_element(By.NAME, "password").send_keys("admin")
    wd.find_element(By.NAME, "login").click()
    yield wd
    wd.quit()


def test_click_all_items(driver):
    driver.implicitly_wait(10)
    for i in range(0, len(driver.find_elements(By.CSS_SELECTOR, "form .row"))):
        countries = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(3)>a")
        countries[i].click()
        zones = driver.find_elements(By.CSS_SELECTOR, '[name*="zone_code"]>[selected="selected"]')
        name_zones = []
        for zone in zones:
            name = zone.text
            name_zones.append(name)
        assert sorted(name_zones) == name_zones, f"Название зон не в алфавитном порядке"
        driver.find_element(By.XPATH, "//*[contains(text(),'Geo Zones')]").click()
