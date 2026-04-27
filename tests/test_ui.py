import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

from Page.MainePageUi import MainPage

load_dotenv()

KINOPOISK_URL = os.getenv("KINOPOISK_URL", "https://www.kinopoisk.ru")


@allure.feature("UI тесты Кинопоиска")
class TestKinopoiskUI:

    @allure.title("Поиск фильма по названию")
    @allure.story("Поиск")
    @pytest.mark.ui
    def test_search_movie(self, browser):
        name = "Интерстеллар"
        main = MainPage(browser)
        main.open()
        main.input_search(name)
        
        assert "Интерстеллар" in browser.page_source

    @allure.title("Поиск с пустым запросом")
    @allure.story("Поиск")
    @pytest.mark.ui
    def test_search_empty(self, browser):
        name = ""
        main = MainPage(browser)
        main.open()
        main.input_search(name)

        
        assert "kinopoisk" in browser.current_url

    @allure.title("Поиск фильма на английском")
    @allure.story("Поиск")
    @pytest.mark.ui
    def test_search_english(self, browser):
        name = "The Sopranos"
        main = MainPage(browser)
        main.open()
        main.input_search(name)

        assert "The Sopranos" in browser.page_source

    @allure.title("Загрузка главной страницы")
    @allure.story("Навигация")
    @pytest.mark.ui
    def test_main_page_load(self, browser):
        browser.get(KINOPOISK_URL)
        assert "Кинопоиск" in browser.title

    @allure.title("Кнопка поиска существует")
    @allure.story("Навигация")
    @pytest.mark.ui
    def test_search_button_exists(self, browser):
        browser.get(KINOPOISK_URL)
        
        wait = WebDriverWait(browser, 45)
        button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        assert button.is_displayed()
