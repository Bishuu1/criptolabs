from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver


def login():
    browser = webdriver.Chrome('/Users/bishuu1/Documents/Github/Cripto/lab2/chromedriver')
    file1 = open('mail-ec.txt', 'r')
    file2 = open('password-ec.txt', 'r')
    browser.get(('https://www.educarchile.cl/user/login'))

    for i in range(20):
        usuario = file1.readline()
        print(usuario)
        contrasena = file2.readline()
        print(contrasena)
        time.sleep(3)
        username = browser.find_element_by_id('edit-name')
        username.clear()
        username.send_keys(usuario)
        time.sleep(2)
        password = browser.find_element_by_id('edit-pass')
        password.clear()
        password.send_keys(contrasena)
        time.sleep(10)
        ingresarButton = browser.find_element_by_id('edit-submit')
        ingresarButton.click()


login()
