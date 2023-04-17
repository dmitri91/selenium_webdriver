from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Driver:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator))

    def staleness_of_elements(self, element, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.staleness_of(element))

    def element_is_invisible(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator))

    def is_element_exists(self, locator):
        elements = self.driver.find_elements(*locator)
        return True if len(elements) > 0 else False

    def open_page(self, url):
        return self.driver.get(url)

