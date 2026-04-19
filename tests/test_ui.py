import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()

KINOPOISK_URL = os.getenv("KINOPOISK_URL", "https://www.kinopoisk.ru")


@allure.feature("UI тесты Кинопоиска")
class TestKinopoiskUI:

    @allure.title("Поиск фильма по названию")
    @allure.story("Поиск")
    @pytest.mark.ui
    def test_search_movie(self, browser):
        browser.get(KINOPOISK_URL)
        
        wait = WebDriverWait(browser, 45)
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "kp_query")))
        search_input.send_keys("Интерстеллар")
        search_input.send_keys(Keys.RETURN)
        
        assert "Интерстеллар" in browser.title

    @allure.title("Поиск с пустым запросом")
    @allure.story("Поиск")
    @pytest.mark.ui
    def test_search_empty(self, browser):
        browser.get(KINOPOISK_URL)
        
        wait = WebDriverWait(browser, 45)
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "kp_query")))
        search_input.send_keys("")
        search_input.send_keys(Keys.RETURN)
        
        assert "kinopoisk" in browser.current_url

    @allure.title("Поиск фильма на английском")
    @allure.story("Поиск")
    @pytest.mark.ui
    def test_search_english(self, browser):
        browser.get(KINOPOISK_URL)
        
        wait = WebDriverWait(browser, 45)
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "kp_query")))
        search_input.send_keys("Inception")
        search_input.send_keys(Keys.RETURN)
        
        assert "Inception" in browser.title or "Начало" in browser.title

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