from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:
    search = '//input[@name="kp_query"]'
    KINOPOISK_URL = os.getenv("KINOPOISK_URL", "https://www.kinopoisk.ru")
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self)-> None:
        self.driver.get(self.KINOPOISK_URL)
        search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.search)))

    def input_search(self, name):
        search_input = self.wait.until(EC.presence_of_element_located((By.NAME, "kp_query")))
        search_input.send_keys(name)
        search_input.send_keys(Keys.RETURN)

