import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@allure.feature("UI тесты Кинопоиска")
class TestKinopoiskUI:

    @allure.title("Поиск по названию. Пример: Ужасающий")
    @allure.story("Поиск фильма")
    @pytest.mark.ui
    def test_search_by_name_terrifier(self) -> None:
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("Ужасающий")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "Ужасающий" in driver.title
        driver.quit()

    @allure.title("Поиск фильма по обрывку названия")
    @allure.story("Поиск фильма")
    @pytest.mark.ui
    def test_search_by_partial_name(self) -> None:
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("Ужаса")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "Ужасающий" in driver.title or "результат" in driver.current_url
        driver.quit()

    @allure.title("Поиск фильма по актеру Тео Джеймс")
    @allure.story("Поиск по актеру")
    @pytest.mark.ui
    def test_search_by_actor(self) -> None:
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("Тео Джеймс")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

        assert "Тео Джеймс" in driver.title or "актер" in driver.current_url
        driver.quit()

    @allure.title("Выбор фильма и просмотр карточки")
    @allure.story("Карточка фильма")
    @pytest.mark.ui
    def test_select_movie_and_view_card(self) -> None:
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("Ярость")
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)

        first_movie = driver.find_element(
            By.XPATH, "(//div[@class='search_results']//a)[1]")
        first_movie.click()
        time.sleep(2)

        assert "Ярость" in driver.title or "фильм" in driver.title
        driver.quit()

    @allure.title("Очистка поисковой строки")
    @allure.story("Поисковая строка")
    @pytest.mark.ui
    def test_clear_search_input(self) -> None:
        driver = webdriver.Chrome()
        driver.get("https://www.kinopoisk.ru")

        input("Пройдите капчу в браузере, затем нажмите Enter...")

        search_input = driver.find_element(By.NAME, "kp_query")
        search_input.send_keys("Ужасающий")
        time.sleep(1)
        search_input.clear()
        time.sleep(1)

        assert search_input.get_attribute("value") == ""
        driver.quit()
