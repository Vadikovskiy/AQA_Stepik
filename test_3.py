from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    letters = string.ascii_lowercase
    for element in elements:
        random_word = ''.join(random.choice(letters) for elements in range(1, 4))
        element.send_keys(random_word)
        #element.send_keys("Мой ответ")


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

print("Задание выполнено! Ответ - 21.23872930526569")

# не забываем оставить пустую строку в конце файла