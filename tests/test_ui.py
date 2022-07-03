import allure

from framework import verify_element_presence


@allure.story("Google")
def test_google(browser):
    browser.open_page("https://google.ru")
    verify_element_presence(browser, "button[class='close-button']")
    verify_element_presence(browser, "input[value='Поиск в Google']")
    browser.check_in_title("Google")


@allure.story("Yandex")
def test_yandex(browser):
    browser.open_page("https://ya.ru")
    verify_element_presence(browser, "#text")
    browser.check_in_title("Яндекс")
