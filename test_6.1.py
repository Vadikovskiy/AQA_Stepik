from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

# Открыть страницу http://suninjuly.github.io/get_attribute.html
browser = webdriver.Chrome()
browser.get(link)

# Посчитать математическую функцию от x (код для этого приведён ниже).


#Считать значение для переменной x

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.ID, "treasure")
element_valuex = x_element.get_attribute("valuex")
print("Значение атрибута valuex: ", element_valuex)
  #assert element_valuex is not None
x = element_valuex
y = calc(x)
calc(x)

  # Ввести ответ в текстовое поле.
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)

# Отметить checkbox "I'm the robot".
checkbox_robot = browser.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox_robot.click()

# Выбрать radiobutton "Robots rule!".
radio_robot = browser.find_element(By.XPATH, "//input[@value='robots']")
radio_robot.click()

# Нажать на кнопку Submit.
submit = browser.find_element(By.XPATH, "//button[@type='submit']")
submit.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
