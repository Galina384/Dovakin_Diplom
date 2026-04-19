import os
import pytest
import allure
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.kinopoisk.dev")
API_TOKEN = os.getenv("API_TOKEN")


def make_request(endpoint: str, token: str = None) -> requests.Response:
    url = f"{API_BASE_URL}{endpoint}"
    headers = {"accept": "application/json"}
    if token:
        headers["X-API-KEY"] = token
    return requests.get(url, headers=headers)


@allure.feature("API тесты Кинопоиска")
class TestKinopoiskAPI:

    @allure.title("Поиск фильма по ID 326")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_get_movie_by_id(self) -> None:
        response = make_request("/v1.4/movie/326", API_TOKEN)
        assert response.status_code == 200
        data = response.json()
        assert data.get("id") == 326

    @allure.title("Поиск по неверному эндпоинту (баг: 200 вместо 404)")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    @pytest.mark.xfail(reason="ответ 200 вместо 404, баг подтвержден")
    def test_invalid_endpoint(self) -> None:
        response = make_request("/v1.4/movies", API_TOKEN)
        assert response.status_code == 404

    @allure.title("Поиск по несуществующему ID")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    def test_nonexistent_id(self) -> None:
        response = make_request("/v1.4/movie/9999999999", API_TOKEN)
        assert response.status_code == 400

    @allure.title("Поиск по названию на кириллице")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_search_cyrillic(self) -> None:
        response = make_request("/v1.4/movie/search?query=во все тяжкие", API_TOKEN)
        assert response.status_code == 200
        data = response.json()
        assert len(data.get("docs", [])) > 0

    @allure.title("Поиск по названию на латинице с ошибкой")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_search_typo(self) -> None:
        response = make_request("/v1.4/movie/search?query=grien mile", API_TOKEN)
        assert response.status_code == 200
        data = response.json()
        assert len(data.get("docs", [])) > 0

    @allure.title("Поиск с пустым запросом (баг: 200 вместо 400)")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    @pytest.mark.xfail(reason="ответ 200 вместо 400, баг подтвержден")
    def test_empty_search(self) -> None:
        response = make_request("/v1.4/movie/search", API_TOKEN)
        assert response.status_code == 400

    @allure.title("Запрос без API-ключа (ожидание 401)")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    def test_no_api_key(self) -> None:
        response = make_request("/v1.4/movie/326", None)
        assert response.status_code == 401

    @allure.title("Запрос с невалидным API-ключом (ожидание 401)")
    @allure.story("Негативные тесты")
    @pytest.mark.api
    def test_invalid_api_key(self) -> None:
        url = f"{API_BASE_URL}/v1.4/movie/search?query=матрица"
        headers = {"X-API-KEY": "invalid_token_12345", "accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 401
        data = response.json()
        assert "Пользователь не найден" in str(data) or "Unauthorized" in str(data)

    @allure.title("Рандомный фильм со статусом post-production")
    @allure.story("Поиск")
    @pytest.mark.api
    def test_random_movie(self) -> None:
        response = make_request("/v1.4/movie/random?type=movie&status=post-production", API_TOKEN)
        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "post-production"
