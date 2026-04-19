import allure
import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.kinopoisk.dev")
API_TOKEN = os.getenv("API_TOKEN")


@allure.feature("API тесты Кинопоиска")
class TestKinopoiskAPI:

    @allure.title("Поиск фильма по ID")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_get_movie_by_id(self):
        url = f"{API_BASE_URL}/v1.4/movie/326"
        headers = {"X-API-KEY": API_TOKEN, "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

    @allure.title("Поиск по неверному эндпоинту (баг)")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    @pytest.mark.xfail(reason="API возвращает 200 вместо 404")
    def test_invalid_endpoint(self):
        url = f"{API_BASE_URL}/v1.4/movies"
        headers = {"X-API-KEY": API_TOKEN, "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 404

    @allure.title("Поиск по несуществующему ID")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    def test_nonexistent_id(self):
        url = f"{API_BASE_URL}/v1.4/movie/9999999999"
        headers = {"X-API-KEY": API_TOKEN, "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 400

    @allure.title("Поиск по названию на кириллице")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_search_cyrillic(self):
        url = f"{API_BASE_URL}/v1.4/movie/search?query=во все тяжкие"
        headers = {"X-API-KEY": API_TOKEN, "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

    @allure.title("Поиск по названию с ошибкой")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_search_typo(self):
        url = f"{API_BASE_URL}/v1.4/movie/search?query=grien mile"
        headers = {"X-API-KEY": API_TOKEN, "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

    @allure.title("Поиск с пустым запросом (баг)")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    @pytest.mark.xfail(reason="API возвращает 200 вместо 400")
    def test_empty_search(self):
        url = f"{API_BASE_URL}/v1.4/movie/search"
        headers = {"X-API-KEY": API_TOKEN, "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 400

    @allure.title("Запрос без API-ключа")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    def test_no_api_key(self):
        url = f"{API_BASE_URL}/v1.4/movie/326"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 401

    @allure.title("Рандомный фильм")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_random_movie(self):
        url = f"{API_BASE_URL}/v1.4/movie/random?type=movie&status=post-production"
        headers = {"X-API-KEY": API_TOKEN, "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
