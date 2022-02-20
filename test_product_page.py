"""

pytest -s -v test_product_page.py

"""
import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()

    # Добавление товара в корзину
    page.add_to_basket()

    # Вычисление матем. выражения
    page.solve_quiz_and_get_code()

    # Проверка названия книги
    page.valid_name_book()

    # Проверка цены книги
    page.valid_price_book()

    time.sleep(10)
