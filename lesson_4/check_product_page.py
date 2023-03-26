import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/en/")
    yield wd
    wd.quit()


def list_value(text):
    value_color = text[5:-1]
    return value_color.split(", ")


def test_check_element_page(driver):
    driver.implicitly_wait(10)
    main_page_name = driver.find_element(By.CSS_SELECTOR, '#box-campaigns .name').text

    main_page_price_regular = driver.find_element(By.CSS_SELECTOR, '.regular-price')
    main_page_price_campaign = driver.find_element(By.CSS_SELECTOR, '.campaign-price')

    main_page_price_regular_text = main_page_price_regular.text
    main_page_price_campaign_text = main_page_price_campaign.text

    tag_line_through_main_regular = main_page_price_regular.get_attribute("tagName")
    color_main_page_price_regular = main_page_price_regular.value_of_css_property("color")

    tag_fatty_text_main = main_page_price_campaign.get_attribute("tagName")
    color_main_page_price_campaign = main_page_price_campaign.value_of_css_property("color")

    size_regular_main = main_page_price_regular.value_of_css_property("font-size")
    size_campaign_main = main_page_price_campaign.value_of_css_property("font-size")

    driver.find_element(By.CSS_SELECTOR, "#box-campaigns .link").click()

    content = driver.find_element(By.CSS_SELECTOR, '#box-product')
    product_page_name = content.find_element(By.CSS_SELECTOR, '.title').text

    product_page_price_regular = content.find_element(By.CSS_SELECTOR, '.regular-price')
    product_page_price_campaign = content.find_element(By.CSS_SELECTOR, '.campaign-price')

    product_page_price_regular_text = product_page_price_regular.text
    product_page_price_campaign_text = product_page_price_campaign.text

    tag_line_through_product_regular = product_page_price_regular.get_attribute("tagName")
    color_product_page_price_regular = product_page_price_regular.value_of_css_property("color")

    tag_fatty_text_product = product_page_price_campaign.get_attribute("tagName")
    color_product_page_price_campaign = product_page_price_campaign.value_of_css_property("color")

    size_regular_product = product_page_price_regular.value_of_css_property("font-size")
    size_campaign_product = product_page_price_campaign.value_of_css_property("font-size")
    # Соответствие текста в заголовке
    assert main_page_name == product_page_name, "Названия товара на главной странице и на странице товара не совпадает"
    # Сответствие цен(обычная и акционная)
    assert main_page_price_regular_text == product_page_price_regular_text, "Несоответвие обычной цены"
    assert main_page_price_campaign_text == product_page_price_campaign_text, "Несоответвие обычной цены"
    # Обычная цена зачеркнута и цвет серый(главная страница)
    assert tag_line_through_main_regular in ['S', 'DEL'], "Цена на главной странице не зачеркнута"
    main_regular = list_value(color_main_page_price_regular)
    assert main_regular[0] == main_regular[1] == main_regular[2], "Цвет обычной цены на главной странице не серый"
    # Обычная цена зачеркнута и цвет серый(страница продукта)
    assert tag_line_through_product_regular in ['S', 'del'], "Цена на странице продукта не зачеркнута"
    product_regular = list_value(color_product_page_price_regular)
    assert product_regular[0] == product_regular[1] == product_regular[2], "Цвет обычной цены на странице продукта не серый"
    # Акционная цена жираная и цвет красный(главная страница)
    assert tag_fatty_text_main in ['B', 'STRONG'], "Акционная цена на главной странице не выделенная"
    product_campaign = list_value(color_main_page_price_campaign)
    assert product_campaign[1] == product_campaign[2] == "0", "Цвет акционной цены на главной странице не красный"
    # Акционная цена жираная и цвет красный(страница продукта)
    assert tag_fatty_text_product in ['B', 'STRONG'], "Акционная цена на странице продукта не выделенная"
    product_campaign = list_value(color_product_page_price_campaign)
    assert product_campaign[1] == product_campaign[2] == "0", "Цвет акционной цены на главной странице не красный"
    # Разница размера текста цен(главная)
    assert float(size_regular_main[:-2]) < float(size_campaign_main[:-2]), "Шрифт акционной цены меньше обычной"
    # Разница размера текста цен(продукта)
    assert float(size_regular_product[:-2]) < float(size_campaign_product[:-2]), "Шрифт акционной цены меньше обычной"
