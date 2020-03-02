import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    input3.send_keys("email")
    input4 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
    input4.send_keys("email")
    input5 = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
    input5.send_keys("email")

    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()