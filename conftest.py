import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language: ru or es or fr or en")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    options = Options()

    if language_name == "ru" or language_name == "es" or language_name == "fr" or language_name == "en":
        print("\nlanguage_name - " + language_name)
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    else:
        raise pytest.UsageError("Введен неопределенный язык (ru, es, fr, en)")

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
