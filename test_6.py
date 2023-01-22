from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

# Открыть страницу https://suninjuly.github.io/math.html
browser = webdriver.Chrome()
browser.get(link)

# Посчитать математическую функцию от x (код для этого приведён ниже).
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Считать значение для переменной x
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
calc(x)

# Ввести ответ в текстовое поле.
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)

# Отметить checkbox "I'm the robot".
checkbox_robot = browser.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox_robot.click()

# Выбрать radiobutton "Robots rule!".
radio_robot = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
radio_robot.click()

# Нажать на кнопку Submit.
submit = browser.find_element(By.XPATH, "//button[@type='submit']")
submit.click()

time.sleep(5)
