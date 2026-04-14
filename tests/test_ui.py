import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestKinopoiskUI:

    @pytest.mark.ui
    def test_search_movie(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("Интерстеллар")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "Интерстеллар" in driver.title
        driver.quit()

    @pytest.mark.ui
    def test_search_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "kinopoisk" in driver.current_url
        driver.quit()

    @pytest.mark.ui
    def test_search_english(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("Inception")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "Inception" in driver.title or "Начало" in driver.title
        driver.quit()

    @pytest.mark.ui
    def test_main_page_load(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        assert "Кинопоиск" in driver.title
        driver.quit()

    @pytest.mark.ui
    def test_search_button_exists(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        button = driver.find_element(By.XPATH, "//button[@type='submit']")
        assert button.is_displayed()
        driver.quit()
