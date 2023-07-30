import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
