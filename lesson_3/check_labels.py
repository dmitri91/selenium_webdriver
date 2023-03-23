import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/en/")
    yield wd
    wd.quit()


def check_count_label(home_page, title):
    elements = home_page.find_elements(By.CSS_SELECTOR, f'{title} li')
    for sticker in elements:
        if not len(sticker.find_elements(By.CSS_SELECTOR, '[class*="sticker"]')) == 1:
            print(f"В заголовке {title} у товара отсутвует стикер")


def test_check_label(driver):
    title = "#box-most-popular"
    check_count_label(driver, title)
    title = "#box-campaigns"
    check_count_label(driver, title)
    title = "#box-latest-products"
    check_count_label(driver, title)


