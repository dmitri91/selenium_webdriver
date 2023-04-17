import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()
