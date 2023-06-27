# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# navigam catre un url
chrome.get("https://formy-project.herokuapp.com/form")

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

'''
exercitiu - maximizam fereastra
toate comenzile incep cu chrome. si sunt intuitive
scrie mai jos chrome. si gandeste-te care ar putea fi comanda corecta
'''
chrome.maximize_window()

# gasim first name dupa ID si scriem valori in formular
chrome.find_element(By.ID, "first-name").send_keys("Bianca")
sleep(3)

# exercitiu: completam impreuna nume apoi punem un sleep de 3 secunde
chrome.find_element(By.ID, "last-name").send_keys("Bad")
sleep(3)

# exercitiu: completeaza singur job title (nu uitam de sleep)
chrome.find_element(By.ID, "job-title").send_keys("junior accountant")
sleep(3)

# exercitiu: select education - nu mai folosim .send_keys() la final. ce metoda crezi ca ar merge aici?
chrome.find_element(By.ID, "radio-button-1").click()
sleep(3)

# exercitiu: select gender (nu uitam de sleep)
chrome.find_element(By.ID, "checkbox-2").click()
sleep(3)

'''
exercitiu: dam click pe submit apoi punem un sleep de 3 secunde
vom invata ce sa facem cand elementul nu are ID
metoda 1: copiem XPATH unic al elementului
metoda 2: intrebam AI https://chat.openai.com/chat
ne va raspunde cu "//a[@class='btn btn-lg btn-primary' and @role='button' and @href='/thanks']"
vezi aici: https://www.itfactory.ro/wp-content/uploads/2023/04/ChatGPT.jpg
'''
chrome.find_element(By.XPATH," /html/body/div/form/div/div[8]/a").click()
sleep(3)

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print("SUCCESS - TEST PASSED")

'''
exercitiu final:
stergem toate comenzile de sleep pentru a vedea viteza testului in timp real
aceasta EFICIENTA ofera o valoare ENORMA si PERMANENTA angajatorilor
costul acestui test tinde spre 0, o data ce a fost scris
asa ca ei vor plati FOARTE BINE o data, ca sa primeasca si sa ramana cu aceasta valoare care ulterior, tinde spre ∞
'''