import time
from selenium.webdriver.common.by import By


link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_reg1 (browser):
    browser.get (link)
    assert browser.find_element (By.CLASS_NAME, "btn-add-to-basket").is_displayed (), f"'Add to basket' button is not displayed"
