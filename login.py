from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Users/igorRamonDev/AppData/Local/Programs/Python/Python311/Scripts/chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver_path)
navegador = webdriver.Chrome(service=chrome_service)

url = 'https://sociogigante.com/home'
navegador.get(url)

email = 'meu-email'
senha = 'minha-senha'

campo_email = navegador.find_element(By.CSS_SELECTOR, '#mat-input-0')
sleep(2)
campo_email.send_keys(email)

campo_senha = navegador.find_element(By.CSS_SELECTOR, '#mat-input-1')
sleep(2)
campo_senha.send_keys(senha)

botao_entrar = navegador.find_element(
    By.CSS_SELECTOR, '.login-btn')
botao_entrar.click()

sleep(15)

navegador.quit()
