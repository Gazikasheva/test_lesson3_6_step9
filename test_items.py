import time
from selenium.webdriver.common.by import By


link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_item_has_add_to_cart_button (browser):
    browser.get (link)
    assert len (browser.find_elements (By.CLASS_NAME, "btn-add-to-basket")) >0, f"'Add to basket' button is not displayed"

