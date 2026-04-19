import os
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
<<<<<<< HEAD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
=======
import time
from dotenv import load_dotenv

load_dotenv()

KINOPOISK_URL = os.getenv("KINOPOISK_URL", "https://www.kinopoisk.ru")
>>>>>>> 3e7d39cbd666fa9c1842bcd97e3fafbb5b374b15


@allure.feature("UI тесты Кинопоиска")
class TestKinopoiskUI:

    @allure.title("Поиск фильма по названию")
    @allure.story("Поиск")
    @pytest.mark.ui
<<<<<<< HEAD
    def test_search_movie(self, driver) -> None:
        wait = WebDriverWait(driver, 15)
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "kp_query")))
=======
    def test_search_movie(self):
        driver = webdriver.Chrome()
        driver.get(KINOPOISK_URL)

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
>>>>>>> 3e7d39cbd666fa9c1842bcd97e3fafbb5b374b15
        search_input.send_keys("Интерстеллар")
        search_input.send_keys(Keys.RETURN)
        
        wait.until(lambda d: "search" in d.current_url)
        assert "Интерстеллар" in driver.page_source

    @allure.title("Поиск с пустым запросом")
    @allure.story("Поиск")
    @pytest.mark.ui
<<<<<<< HEAD
    def test_search_empty(self, driver) -> None:
        wait = WebDriverWait(driver, 15)
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "kp_query")))
=======
    def test_search_empty(self):
        driver = webdriver.Chrome()
        driver.get(KINOPOISK_URL)

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
>>>>>>> 3e7d39cbd666fa9c1842bcd97e3fafbb5b374b15
        search_input.send_keys("")
        search_input.send_keys(Keys.RETURN)
        
        assert "kinopoisk" in driver.current_url

    @allure.title("Поиск фильма на английском языке")
    @allure.story("Поиск")
    @pytest.mark.ui
<<<<<<< HEAD
    def test_search_english(self, driver) -> None:
        wait = WebDriverWait(driver, 15)
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "kp_query")))
=======
    def test_search_english(self):
        driver = webdriver.Chrome()
        driver.get(KINOPOISK_URL)

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
>>>>>>> 3e7d39cbd666fa9c1842bcd97e3fafbb5b374b15
        search_input.send_keys("Inception")
        search_input.send_keys(Keys.RETURN)
        
        wait.until(lambda d: "search" in d.current_url)
        assert "Inception" in driver.page_source or "Начало" in driver.page_source

    @allure.title("Загрузка главной страницы")
    @allure.story("Навигация")
    @pytest.mark.ui
<<<<<<< HEAD
    def test_main_page_load(self, driver) -> None:
=======
    def test_main_page_load(self):
        driver = webdriver.Chrome()
        driver.get(KINOPOISK_URL)

        input("Пройдите капчу в браузере, затем нажмите Enter...")

>>>>>>> 3e7d39cbd666fa9c1842bcd97e3fafbb5b374b15
        assert "Кинопоиск" in driver.title

    @allure.title("Проверка наличия кнопки поиска")
    @allure.story("Навигация")
    @pytest.mark.ui
<<<<<<< HEAD
    def test_search_button_exists(self, driver) -> None:
        wait = WebDriverWait(driver, 15)
        button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        assert button.is_displayed()
=======
    def test_search_button_exists(self):
        driver = webdriver.Chrome()
        driver.get(KINOPOISK_URL)

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        button = driver.find_element(By.XPATH, "//button[@type='submit']")
        assert button.is_displayed()
        driver.quit()

>>>>>>> 3e7d39cbd666fa9c1842bcd97e3fafbb5b374b15
