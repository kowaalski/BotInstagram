from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait #Se espera a actuar hasta que toda la pagina esta cargada.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from termcolor import colored, cprint
import random


user="cardigarciagonzalez@gmail.com"
password="cardi1234GG"
link_Sorteo='https://www.instagram.com/p/Cjccieuq5gt/'

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option("excludeSwitches", ["enable-automation"]) #2 lineas estas, para que no se muestre en chrome que se esta usando un software automatizado
options.add_experimental_option('useAutomationExtension', False)

s = Service('C:\\Users\\DIEGO\\Documents\\Programas\\BotInstagram\\chromeDriver\\chromedriver.exe') #La ruta del chromeDriver.exe
bot = webdriver.Chrome(service=s, options=options)


bot.get(link_Sorteo) 
time.sleep(4)


bot.refresh()


