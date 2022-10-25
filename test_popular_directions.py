"""
!!!
Реализован UI авто-тест на предлагаемые популярные направления, находящиеся
под формой поиска на главной странице Web-desktop aviata.kz:

Тест 1. Проверяется появление строки 'Популярные направления' после
клика в поле 'Откуда'

Тест 2. Проверяется количество популярных направлений в выпадающем
списке равно 7
!!!
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BROWSER = webdriver.Chrome()
URL = "https://aviata.kz/"
WAIT = WebDriverWait(BROWSER, 500)


def popular_directions_appearance(URL):
    # ожидаем появления выпадающего списка после клика в поле 'Откуда'
    BROWSER.get(URL)
    select_from = BROWSER.find_element(By.CSS_SELECTOR, "[placeholder='Откуда']")
    select_from.click()
    WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME, "city-search-modal")))


def number_of_popular_directions():
    # считаем количество популярных направлений в выпадающем списке
    directions = BROWSER.find_elements(By.CLASS_NAME, 'ux-search-history-item-selected')
    return int(len(directions))


try:
    # Тест 1. Проверка появления строки 'Популярные направления' после клика в поле 'Откуда'
    popular_directions_appearance(URL)
    assert 'Популярные направления' in BROWSER.find_element(By.TAG_NAME, "h3").text, 'Test 1: FAILED'
    # выводим результат в консоль
    if 'Популярные направления' in BROWSER.find_element(By.TAG_NAME, "h3").text:
        print('Test 1: PASSED')
    
    # Тест 2. Проверка: количество популярных направлений в выпадающем списке равно 7
    num = number_of_popular_directions()
    assert num == 7, 'Test 2: FAILED'
    # выводим результат в консоль
    if num == 7:
        print('Test 2: PASSED')


finally:
    # делаем паузу для удобства просмотра за тестом
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    BROWSER.quit()
