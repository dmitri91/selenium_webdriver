import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    wd.find_element(By.NAME, "username").send_keys("admin")
    wd.find_element(By.NAME, "password").send_keys("admin")
    wd.find_element(By.NAME, "login").click()
    yield wd
    wd.quit()


def there_is_window_other_than(old_win):
    def _fun(driver):
        handles = driver.window_handles
        for i in old_win:
            handles.remove(i)
        return handles[0] if len(handles) > 0 else False
    return _fun


def test_new_window(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//a[contains(text(), 'Antarctica')]").click()
    els = driver.find_elements(By.CSS_SELECTOR, 'form [target="_blank"]')
    for i in range(0, len(els)):
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        els = driver.find_elements(By.CSS_SELECTOR, 'form [target="_blank"]')
        els[i].click()
        new_window = wait.until(there_is_window_other_than(old_windows))
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(main_window)
