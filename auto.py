from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# abre o chorme
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Vai para o site:
driver.get('https://zlliu246.github.io/test-site')

#Não faz nada por 1s
sleep(1)

# Encontra o botão por  class_name
button = driver.find_element(By.CLASS_NAME, 'my-button')

# clica no botão por 5 vez (intervalo:1s) 
for i in range(4):
    button.click()
    sleep(1)

#Nâo faz nada por 5 segundos 
sleep(5)

#sai do driver 
driver.quit()