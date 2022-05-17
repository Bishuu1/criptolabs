from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver


def login():
    browser = webdriver.Chrome('/Users/bishuu1/Documents/Github/Cripto/chromedriver')
    usernameStr = 'usuario@usuario'
    passwordStr = 'contrasena'

    browser.get(('https://www.cinemark.cl/#signin'))
    time.sleep(5)
    username = browser.find_element_by_id('username')
    username.send_keys(usernameStr)
    password = browser.find_element_by_id('password')
    password.send_keys(passwordStr)
    time.sleep(5)
    ingresarButton = browser.find_element(by=By.XPATH, value="//input[@value='Entrar']")
    ingresarButton.click()


def signup():
    browser = webdriver.Chrome('/Users/bishuu1/Documents/Github/Cripto/chromedriver')
