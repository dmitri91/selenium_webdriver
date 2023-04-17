from selenium.webdriver.common.by import By
from driver import Driver
class HomePage(Driver):
    FIRST_ITEM_TO_LIST = (By.CSS_SELECTOR, '.listing-wrapper a')
    HOME_BUTTON = (By.CSS_SELECTOR, '.general-0 a')
    BASKET_BUTTON = (By.CSS_SELECTOR, '#cart .link')


    def open_item(self, locator):
        self.find_element(locator).click()

    def return_to_home(self):
        self.find_element(self.HOME_BUTTON).click()

    def open_basket(self):
        self.find_element(self.BASKET_BUTTON).click()

class ProductPage(Driver):
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[name="add_cart_product"]')
    def add_product(self):
        self.find_element(self.ADD_PRODUCT_BUTTON).click()

class BasketPage(Driver):
    DATA_TABLE = (By.CSS_SELECTOR, '#box-checkout-summary tbody')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '[name="remove_cart_item"]')
    ALL_ELEMENTS_IN_TABLE = (By.CSS_SELECTOR, '.dataTable .item')

    def check_amount_in_basket(self, i):
        self.find_element((By.XPATH, f"//*[@class='quantity'][contains(text(),'{i}')]"))


    def delete_items(self):
        elements = self.find_elements(self.ALL_ELEMENTS_IN_TABLE)
        for _ in range(1, len(elements)):
            data_table = self.find_element(self.DATA_TABLE)
            self.find_element(self.REMOVE_BUTTON).click()
            self.staleness_of_elements(data_table)
