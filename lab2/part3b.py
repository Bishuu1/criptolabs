from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
import requests
import re
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def newmail():
    # get mail
    URL = 'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1'
    data = requests.get(URL)
    data = data.json()
    mail = data[0]
    file1 = open('mail_generado_eu.txt', 'a')
    file1.write(mail)
    file1.write("\n")
    file1.close()
    return mail


def signup():
    # get mail
    mail = newmail()
    browser = webdriver.Chrome('/Users/bishuu1/Documents/Github/Cripto/lab2/chromedriver')
    browser.get(('https://www.normacomics.com/customer/account/create/'))
    time.sleep(5)
    firstname = browser.find_element(By.ID, "firstname")
    time.sleep(5)
    firstname.send_keys('Juanin')
    lastname = browser.find_elements(By.XPATH, '//*[@id="lastname"]')
    lastname[0].send_keys('Juanjarry')
    email = browser.find_elements(By.XPATH, '//*[@id="email_address"]')
    email[0].send_keys(mail)
    password = browser.find_elements(By.XPATH, '//*[@id="password"]')
    password[0].send_keys('contrasena')
    password2 = browser.find_elements(By.XPATH, '//*[@id="confirmation"]')
    password2[0].send_keys('contrasena')
    time.sleep(15)
    checkbox = browser.find_elements(By.XPATH, '//*[@id="is_subscribed"]')
    checkbox[0].click()
    time.sleep(4)
    button = browser.find_elements(By.XPATH, '//*[@id="form-validate"]/div[4]/button/span/span')
    button[0].click()
    time.sleep(5)


def login():
    browser = webdriver.Chrome('/Users/bishuu1/Documents/Github/Cripto/lab2/chromedriver')
    filea = open('mail_generado_eu.txt', 'r')
    email = filea.readline()
    browser.get(('https://www.normacomics.com/customer/account/login/'))
    time.sleep(5)
    password = browser.find_elements(By.XPATH, '//*[@id="pass"]')
    password[0].send_keys('contrasena')
    username = browser.find_elements(By.XPATH, '//*[@id="email"]')
    username[0].send_keys(email)
    time.sleep(5)
    objeto = []
    objeto.append(browser)
    objeto.append(email)
    objeto.append('contrasena')
    return objeto


def reset():
    file1 = open('mail_generado_eu.txt', 'r')
    email = file1.readline()
    local, at, domain = email.rpartition('@')
    browser = webdriver.Chrome('/Users/bishuu1/Documents/Github/Cripto/lab2/chromedriver')
    txt = "https://www.1secmail.com/?login=demo&domain=dominio"
    x = re.sub("demo", local, txt)
    x = re.sub("dominio", domain, x)
    browser.get((x))
    time.sleep(2)

    # make new tab
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(('https://www.normacomics.com/customer/account/forgotpassword/'))
    time.sleep(2)
    email1 = browser.find_elements(By.XPATH, '//*[@id="email_address"]')
    email1[0].send_keys(email+Keys.ENTER)
    time.sleep(15)
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(5)
    correoRecived = browser.find_elements(By.XPATH, '//*[@id="content"]/div/table/tbody/tr[2]')
    correoRecived[0].click()
    correoReset = browser.find_elements(
        By.XPATH, '//*[@id="messageBody"]/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/p[2]/a')
    correoReset[0].click()
    correo = browser.find_elements(By.XPATH, '//*[@id="password"]')
    correo[0].send_keys('contrasena')
    correo2 = browser.find_elements(By.XPATH, '//*[@id="confirmation"]')

    time.sleep(10)
    correo2[0].send_keys('contrasena' + Keys.ENTER)
    time.sleep(10)


def modify():
    retorno = login()
    browser = retorno[0]
    email = retorno[1]
    password = retorno[2]
    correoReset = browser.find_elements(
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/p/a')
    correoReset[0].click()
    current_password = browser.find_elements(By.XPATH, '//*[@id="current_password"]')
    current_password[0].send_keys(password)
    new_password = browser.find_elements(By.XPATH, '//*[@id="password"]')
    new_password[0].send_keys('contrasena1')
    new_password2 = browser.find_elements(By.XPATH, '//*[@id="confirmation"]')
    new_password2[0].send_keys('contrasena1')
    time.sleep(30)
    browser.find_elements(By.XPATH, '//*[@id="agreement-news"]')[0].click()
    time.sleep(15)
    ingresarButton = browser.find_elements(By.XPATH, '//*[@id="form-validate"]/div[3]/button/span/span')
    ingresarButton[0].click()


modify()
