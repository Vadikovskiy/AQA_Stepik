from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

    # Открыть страницу https://suninjuly.github.io/selects1.html
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

# def calc(x, y):
#   return str(x + y)

    #Посчитать сумму заданных чисел
element_num1 = browser.find_element(By.XPATH, "//span[@id='num1']")
element_num2 = browser.find_element(By.XPATH, "//span[@id='num2']")
x = element_num1.text
y = element_num2.text
i = int(x) + int(y)
# calc(x, y)

print(x)
print(y)
print(i)


  # Ввести ответ в текстовое поле.
answer = browser.find_element(By.XPATH, "//select[@id='dropdown']")
answer.send_keys(i)

# Нажать на кнопку Submit.
submit = browser.find_element(By.XPATH, "//button[@type='submit']")
submit.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()