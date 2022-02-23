"""

pytest -s -v test_product_page.py

"""
import time

import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize(
    'link',
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     pytest.param(
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
         marks=pytest.mark.xfail
     ),
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
     ]
)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    print(link)

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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    print(link)

    page = ProductPage(browser, link, 0)
    page.open()

    # Добавление товара в корзину
    page.add_to_basket()

    # Проверка на отсутствие сообщения об успехе
    page.should_not_be_success_message()

    time.sleep(10)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    print(link)

    page = ProductPage(browser, link, 0)
    page.open()

    # Проверка на отсутствие сообщения об успехе
    page.should_not_be_success_message()

    time.sleep(10)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    print(link)

    page = ProductPage(browser, link, 0)
    page.open()

    # Добавление товара в корзину
    page.add_to_basket()

    # Проверка на исчезновение сообщения об успехе
    page.should_disappearance_success_message()

    time.sleep(10)
