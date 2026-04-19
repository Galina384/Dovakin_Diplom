import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.kinopoisk.ru")

input("Пройдите капчу вручную, затем нажмите Enter...")

# Ждем, пока загрузится главная страница
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Кинопоиск"))

# Сохраняем cookies
cookies = driver.get_cookies()
with open('cookies.json', 'w') as f:
    json.dump(cookies, f)

print(f"Сохранено {len(cookies)} cookies")
driver.quit()
