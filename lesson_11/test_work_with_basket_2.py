from pages import BasketPage, HomePage, ProductPage


def test_delete_duck_from_basket(browser):
    basket_page = BasketPage(browser)
    home_page = HomePage(browser)
    product_page = ProductPage(browser)
    home_page.open_page('http://localhost/litecart/en/')
    for i in range(1, 4):
        home_page.open_item(home_page.FIRST_ITEM_TO_LIST)
        product_page.add_product()
        basket_page.check_amount_in_basket(i)
        home_page.return_to_home()
    home_page.open_basket()
    basket_page.delete_items()
