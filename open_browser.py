import time
from selenium import webdriver
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://www.litres.ru/")
textinput = driver.find_element_by_css_selector("[class=\"Search-module__input\"]")
textinput.send_keys("Айзек Азимов")
submit_button = driver.find_element_by_css_selector("[class=\"Search-module__button\"]")
submit_button.click()
time.sleep(5)
driver.quit()