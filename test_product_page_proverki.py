import pytest
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By

# 1. Тест: сообщение об успехе не отображается до добавления товара
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(By.CSS_SELECTOR, "#messages .alert-success"), \
        "Success message is visible before product is added to basket"

# 2. Тест: сообщение не появляется после добавления товара (ожидаемый баг — пометим xfail)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(By.CSS_SELECTOR, "#messages .alert-success"), \
        "Success message is displayed after adding to basket, but should not be"

# 3. Тест: сообщение исчезает после добавления товара (ожидаемый баг — пометим xfail)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(By.CSS_SELECTOR, "#messages .alert-success"), \
        "Success message did not disappear after appearing"

