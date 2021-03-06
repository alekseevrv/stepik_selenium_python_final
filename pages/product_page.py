from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def valid_name_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        name_book_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_BASKET)

        assert name_book_basket.text == name_book.text, \
            "Product name does not match the product added"

    def valid_price_book(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price_book_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_BASKET)

        assert price_book_basket.text == price_book.text, \
            "The price of the cart does not match the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappearance_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappearance"
