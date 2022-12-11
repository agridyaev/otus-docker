import allure

from framework import verify_element_presence


@allure.story("DuckDuckGo")
def test_duckduckgo(browser):
    browser.open_page("https://duckduckgo.com/")
    verify_element_presence(browser, "input[id='search_form_input_homepage']")
    verify_element_presence(browser, "input[id='search_button_homepage']")
    browser.check_in_title("DuckDuckGo")


@allure.story("Yandex")
def test_yandex(browser):
    browser.open_page("https://ya.ru/")
    verify_element_presence(browser, "#text")
    browser.check_in_title("Яндекс")
