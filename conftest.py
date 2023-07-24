import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")
#
#


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Specify the language for the browser")


@pytest.fixture(scope="module")
def browser(request):
    # Читаем параметр language из командной строки
    language = request.config.getoption("--language")
    # Создаем объект ChromeOptions для настройки языка
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Инициализируем браузер с заданными опциями
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    # Закрываем браузер после завершения тестов
    browser.quit()

# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
