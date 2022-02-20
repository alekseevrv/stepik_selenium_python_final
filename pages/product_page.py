from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def valid_name_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        name_book_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_BASKET)

        assert name_book_basket.text.find(name_book.text) != -1, \
            "Product name does not match the product added"

    def valid_price_book(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price_book_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_BASKET)

        assert price_book_basket.text.find(price_book.text) != -1, \
            "The price of the cart does not match the price of the product"
