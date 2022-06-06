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
from selenium.webdriver.chrome.options import Options


def newmail():
    # get mail
    URL = 'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1'
    data = requests.get(URL)
    data = data.json()
    mail = data[0]
    file1 = open('mail_generado.txt', 'w')
    file1.write(mail)
    # file1.write("\n")
    file1.close()
    return mail


def login():
    op = Options()
    op.add_extension('/Users/bishuu1/Documents/Github/Cripto/lab2/AdBlock-—-best-ad-blocker.crx')
    browser = webdriver.Chrome(executable_path='/Users/bishuu1/Documents/Github/Cripto/lab2/chromedriver', options=op)
    filea = open('mail_generado.txt', 'r')
    email = filea.readline()
    browser.get(('https://www.cinemark.cl/#signin'))
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])
    password = browser.find_elements(By.XPATH, '//*[@id="password"]')
    password[0].send_keys('contrasena')
    username = browser.find_elements(By.XPATH, '//*[@id="username"]')
    username[0].send_keys(email)
    ingresarButton = browser.find_elements(By.XPATH, '//*[@id="modyo-session-oauth2"]/form/input[2]')
    ingresarButton[0].click()
    objeto = []
    objeto.append(browser)
    objeto.append(email)
    objeto.append('contrasena')
    time.sleep(10)
    return objeto

    # time.sleep(10)


def signup():
    op = Options()
    op.add_extension('/Users/bishuu1/Documents/Github/Cripto/lab2/AdBlock-—-best-ad-blocker.crx')
    browser = webdriver.Chrome(executable_path='/Users/bishuu1/Documents/Github/Cripto/lab2/chromedriver', options=op)
    # get ruts
    browser.get(('https://sandbox.goodweb.cl/generador-de-ruts/?'))
    browser.switch_to.window(browser.window_handles[0])
    findRut = browser.find_element_by_id('enviar')
    findRut.click()
    time.sleep(3)
    copiarRut = browser.find_element(by=By.XPATH, value="//input[@value='Copiar']")
    copiarRut.click()

    # get mail
    mail = newmail()

    # make new tab
    browser.switch_to.window(browser.window_handles[1])

    # register new user
    browser.get(('https://www.cinemark.cl/registro'))
    cookies = browser.find_elements(By.XPATH, '//*[@id="modal-cookies-template"]/div[1]/div/button')
    if(cookies):
        cookies[0].click()
    time.sleep(2)
    name = browser.find_element_by_id('firstname')
    name.send_keys('Juanin')
    lastname = browser.find_element_by_id('lastname')
    lastname.send_keys('Juanjarry')
    time.sleep(1)

    rut = browser.find_element_by_id('docu1')
    rut.send_keys(Keys.COMMAND+"v")
    time.sleep(1)
    select = browser.find_elements(By.XPATH, '//*[@id="form-elitegold"]/div/div/div[4]/div[1]/div/div[1]/select')
    day = Select(select[0])
    day.select_by_value('03')
    select = browser.find_elements(By.XPATH, '//*[@id="form-elitegold"]/div/div/div[4]/div[1]/div/div[2]/select')
    month = Select(select[0])
    month.select_by_value('03')
    select = browser.find_elements(By.XPATH, '//*[@id="form-elitegold"]/div/div/div[4]/div[1]/div/div[3]/select')
    year = Select(select[0])
    year.select_by_value('2000')
    email = browser.find_element_by_id('email1')
    email.send_keys(mail)
    email2 = browser.find_element_by_id('email2')
    email2.send_keys(mail)
    phone = browser.find_element(by=By.XPATH, value="//input[@title='Completa este campo con tu teléfono']")
    phone.send_keys('92345678')
    password = browser.find_element_by_id('pass1')
    password.send_keys('contrasena')
    password2 = browser.find_element_by_id('pass2')
    password2.send_keys('contrasena')
    time.sleep(5)
    inscribir = browser.find_element(by=By.XPATH, value='//*[@id="form-elitegold"]/div/div/div[10]/button')
    inscribir.click()

    time.sleep(10)


def reset():
    file1 = open('mail_generado.txt', 'r')
    email = file1.readline()
    local, at, domain = email.rpartition('@')
    op = Options()
    op.add_extension('/Users/bishuu1/Documents/Github/Cripto/lab2/AdBlock-—-best-ad-blocker.crx')
    browser = webdriver.Chrome(executable_path='/Users/bishuu1/Documents/Github/Cripto/lab2/chromedriver', options=op)
    txt = "https://www.1secmail.com/?login=demo&domain=dominio"
    x = re.sub("demo", local, txt)
    x = re.sub("dominio", domain, x)
    browser.get((x))
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)

    # make new tab
    browser.switch_to.window(browser.window_handles[1])
    browser.get(('https://www.cinemark.cl/reset-password'))
    time.sleep(2)
    cookies = browser.find_elements(By.XPATH, '//*[@id="modal-cookies-template"]/div[1]/div/button')
    cookies[0].click()

    email1 = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/p/input')
    email1[0].send_keys(email)
    botoningresar = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[1]/div[3]/button')
    botoningresar[0].click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])
    correoRecived = browser.find_elements(By.XPATH, '//*[@id="content"]/div/table/tbody/tr[2]')
    correoRecived[0].click()
    time.sleep(10)
    correoReset = browser.find_elements(By.XPATH, '//*[@id="messageBody"]/div/a')
    correoReset[0].click()
    print('ahora!')
    adbutton = browser.find_elements(By.XPATH, '//*[@id="dismiss-button"]/div/span')
    if(adbutton):
        adbutton[0].click()
    time.sleep(10)
    passworda = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[2]/div[3]/p/input')
    passwordb = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[2]/div[4]/p[1]/input')
    time.sleep(3)
    passworda[0].send_keys('contrasena')
    passwordb[0].send_keys('contrasena')
    time.sleep(10)
    botoningresar = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[2]/div[5]/button')
    botoningresar[0].click()
    time.sleep(10)


def modify():
    retorno = login()
    browser = retorno[0]
    email = retorno[1]
    contrasena = retorno[2]
    cookies = browser.find_elements(By.XPATH, '//*[@id="modal-cookies-template"]/div[1]/div/button')
    cookies[0].click()
    time.sleep(3)
    tab = browser.find_elements(By.XPATH, '//*[@id = "tabs-me"]/ul/li[2]/a')
    tab[0].click()
    time.sleep(2)
    form = browser.find_elements(By.XPATH, '//*[@id = "form-elitegold"]/div/div[2]/div[6]/div/div/div/div[2]/label/a')
    form[0].click()
    time.sleep(3)
    email1 = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/p/input')
    email1[0].send_keys(email)
    botoningresar = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[1]/div[3]/button')
    botoningresar[0].click()
    time.sleep(3)
    # Abrir correo en otra tab
    browser.switch_to.window(browser.window_handles[1])
    local, at, domain = email.rpartition('@')
    txt = "https://www.1secmail.com/?login=demo&domain=dominio"
    x = re.sub("demo", local, txt)
    x = re.sub("dominio", domain, x)
    browser.get((x))
    time.sleep(5)
    refresh = browser.find_elements(By.XPATH, '//*[@id="refreshMailBtn"]')
    refresh[0].click()
    time.sleep(3)
    correoRecived = browser.find_elements(By.XPATH, '//*[@id="content"]/div/table/tbody/tr[2]')
    correoRecived[0].click()
    correoReset = browser.find_elements(By.XPATH, '//*[@id="messageBody"]/div/a')
    correoReset[0].click()
    passworda = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[2]/div[3]/p/input')
    passwordb = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[2]/div[4]/p[1]/input')
    time.sleep(2)
    passworda[0].send_keys('contrasena')
    passwordb[0].send_keys('contrasena')
    time.sleep(3)
    botoningresar = browser.find_elements(
        By.XPATH, '//*[@id="password-container"]/div/div[2]/div[1]/div[2]/div[2]/div[5]/button')
    botoningresar[0].click()
    time.sleep(5)

signup()
modify()
reset()