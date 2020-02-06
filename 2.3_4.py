from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
    x = x_element.text
    x = int(x)
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit(10)