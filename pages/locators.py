from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators:
    BASKET_LINK = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    NAME_BOOK = (By.XPATH, "//div[contains(@class,'product_main')]/child::h1")
    NAME_BOOK_BASKET = (By.XPATH, "//div[contains(@class,'alertinner')]/child::strong[1]")
    PRICE_BOOK = (By.XPATH, "//div[contains(@class,'product_main')]/child::p[1]")
    PRICE_BOOK_BASKET = (By.XPATH, "//div[contains(@class,'alertinner')]/child::p/strong")
