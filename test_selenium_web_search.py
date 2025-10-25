import os

import allure
import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from helpers import wait_for_element

load_dotenv()

selenium_url = os.getenv("SELENIUM_BASE_URL")
google_url = os.getenv("GOOGLE_BASE_URL")
duck_url = os.getenv("DUCKDUCKGO_BASE_URL")


@pytest.mark.ui
@allure.title("Открытие сайта Selenium")
@allure.description("Проверка, что сайт selenium.dev открывается и содержит корректный заголовок.")
def test_selenium_web(driver):
    with allure.step("Открыть сайт Selenium"):
        driver.get(selenium_url)

    with allure.step("Проверить, что открыта правильная страница"):
        assert driver.current_url == selenium_url
        assert 'Selenium' in driver.title


@pytest.mark.ui
@allure.title("DuckDuckGo: поиск Selenium")
@allure.description("Поиск Selenium в DuckDuckGo и переход на selenium.dev.")
def test_duckduckgo_search_selenium(driver):
    with allure.step("Открыть DuckDuckGo"):
        driver.get(duck_url)

    with allure.step("Ввести запрос 'Selenium'"):
        field = wait_for_element(driver, By.NAME, "q", "clickable")
        field.send_keys("Selenium", Keys.ENTER)

    with allure.step("Кликнуть по ссылке на selenium.dev"):
        link = wait_for_element(
            driver,
            By.CSS_SELECTOR,
            'a[data-testid="result-title-a"][href*="selenium.dev"]',
            "clickable",
        )
        link.click()

    with allure.step("Проверить, что открыта страница Selenium"):
        wait_for_element(driver, By.TAG_NAME, "body", "visible")
        assert "selenium.dev" in driver.current_url
        assert "Selenium" in driver.title


@pytest.mark.ui
@allure.title("Google: поиск Selenium")
@allure.description("Поиск Selenium в Google и переход на selenium.dev.")
def test_google_search_selenium(driver):
    with allure.step("Открыть Google"):
        driver.get(f"{google_url}?hl=ru&gl=ru")

    with allure.step("Ввести запрос 'Selenium'"):
        field = wait_for_element(driver, By.NAME, "q", "clickable")
        field.send_keys("Selenium", Keys.ENTER)

    with allure.step("Кликнуть по ссылке на selenium.dev"):
        link = wait_for_element(
            driver,
            By.CSS_SELECTOR,
            "a[jsname='UWckNb'][href*='selenium.dev']",
            "clickable",
        )
        link.click()

    with allure.step("Проверить, что открыта страница Selenium"):
        wait_for_element(driver, By.TAG_NAME, "body", "visible")
        assert "selenium.dev" in driver.current_url
        assert "Selenium" in driver.title
