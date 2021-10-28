import time
from selenium import webdriver


def OpenLitres(driver):
    '''
        Open https://www.litres.ru/ in Google Chrome
        and search Isaac Asimov's books

    '''
    driver.get("https://www.litres.ru/")
    textinput = driver.find_element_by_css_selector("[class=\"Search-module__input\"]")
    textinput.send_keys("Айзек Азимов")
    submit_button = driver.find_element_by_css_selector("[class=\"Search-module__button\"]")
    submit_button.click()
    time.sleep(5)
    driver.quit()


def OpenGoogle(driver):
    '''
        Open https://www.google.com/ in Google Chrome
        and search info about Isaac Asimov
        
    '''
    driver.get("https://www.google.com/")
    textinput = driver.find_element_by_css_selector("[class=\"gLFyf gsfi\"]")
    textinput.send_keys("Айзек Азимов")
    submit_button = driver.find_elements_by_css_selector("[class=\"gNO89b\"]")
    submit_button[-1].click()
    time.sleep(5)
    driver.quit()


def OpenYandex(driver):
    '''
        Open https://www.yandex.ru/ in Google Chrome
        and search info about Isaac Asimov
        
    '''
    driver.get("https://www.yandex.ru/")
    textinput = driver.find_element_by_id("text")
    textinput.send_keys("Айзек Азимов")
    submit_button = driver.find_element_by_css_selector(".search2__button [role=\"button\"]")
    submit_button.click()
    time.sleep(5)
    driver.quit()


driver = webdriver.Chrome()
time.sleep(5)
OpenYandex(driver)