# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://www.instagram.com/')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# vrem sa dam click pe accept cookies
chrome.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]').click()
sleep(3)

# completam username
chrome.find_element(By.XPATH, '//input[@name="username"]').send_keys('user123')
sleep(3)

# completam password
chrome.find_element(By.XPATH, '//input[@name="password"]').send_keys('pass123')
sleep(3)

# dam click pe login
chrome.find_element(By.XPATH, '//button[@type="submit"]').click()
sleep(3)

# salvam textul din mesajul de eroare
mesaj_eroare = chrome.find_element(By.XPATH, '//p[@id="slfErrorAlert"]').text
assert mesaj_eroare == 'Sorry, your password was incorrect. Please double-check your password.'

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')
