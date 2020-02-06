from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
message = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
x = x_element.text
x = int(x)
y = calc(x)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_xpath('//*[@id="answer"]')
input1.send_keys(y)

# Отправляем заполненную форму
button = browser.find_element_by_xpath('/html/body')
button.click()

