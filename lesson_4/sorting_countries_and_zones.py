import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    wd.find_element(By.NAME, "username").send_keys("admin")
    wd.find_element(By.NAME, "password").send_keys("admin")
    wd.find_element(By.NAME, "login").click()
    yield wd
    wd.quit()


def test_sorting_countries_and_zones(driver):
    driver.implicitly_wait(10)
    countries_with_zones = []
    name_country = []
    countries = driver.find_elements(By.CSS_SELECTOR, ".dataTable tr.row")
    for country in countries:
        name = country.find_element(By.CSS_SELECTOR, "a").text
        name_country.append(name)
        if country.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text != "0":
            countries_with_zones.append(name)
    assert sorted(name_country) == name_country, f"Название стран не в алфавитном порядке"
    for i in countries_with_zones:
        name_zones = []
        driver.find_element(By.XPATH, f"//*[contains(text(),'{i}')]").click()
        zones = driver.find_elements(By.CSS_SELECTOR, '.dataTable td:nth-child(3)')
        zones.pop()
        for zone_2 in zones:
            zone_name = zone_2.text
            name_zones.append(zone_name)
        driver.find_element(By.XPATH, "//*[contains(text(),'Countries')]").click()
        assert sorted(name_zones) == name_zones, f"Название зон в блоке {i} не в алфавитном порядке"
