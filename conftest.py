import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv()

KINOPOISK_URL = os.getenv("KINOPOISK_URL", "https://www.kinopoisk.ru")


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get(KINOPOISK_URL)
    
    # Загружаем cookies
    try:
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        print("Cookies загружены")
    except FileNotFoundError:
        print("Файл cookies.json не найден")
    
    yield driver
    driver.quit()
