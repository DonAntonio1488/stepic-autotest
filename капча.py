import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Нажимаем на кнопку  и переходим на новую вкладку
    button1 = browser.find_element_by_css_selector("button.btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Ищем х и вводим ответ в поле
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
	
    
    # Отправляем  форму
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

    # ждем загрузки страницы
    time.sleep(1)

    

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
