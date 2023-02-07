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



def log_in():
    try:
    
        #Si en 5s, no carga la pagina lanza excepcion. Espera a darle click hasta que carga la pagina con un maximo de 5s, el enlace de xpath es donde hacemos click, lo scamos inspeccionando elemento, copy FULL XPATH
        
        #Aceptar cookies
        WebDriverWait(bot, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/button[2]')))\
            .click()
        delay()
        cprint('COKIES ACEPTED','green')

        #Mete usuario
        WebDriverWait(bot, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')))\
            .send_keys(user)
        
        delay()
        cprint('USER ENTERED','green')

        #Mete password
        WebDriverWait(bot, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')))\
            .send_keys(password)

        delay()
        cprint('PASSWORD ENTERED','green')

        #Click enter
        WebDriverWait(bot, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')))\
            .click()
        cprint('LOGGED IN','green',attrs=['bold','blink'])

    except:
        cprint('ERROR: timeOut','red')


def delay():
    time.sleep(random.uniform(1, 3))

def configureBot(): #Configuramos selenium
    
    # Opciones de navegación (Para indicar como queremos que se inicie el navegador)
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_experimental_option('excludeSwitches', ['enable-automation','enable-logging']) #2 lineas estas, para que no se muestre en chrome que se esta usando un software automatizado
    options.add_experimental_option('useAutomationExtension', False)

    s = Service('C:\\Users\\DIEGO\\Documents\\Programas\\BotInstagram\\chromeDriver\\chromedriver.exe') #La ruta del chromeDriver.exe
    bot = webdriver.Chrome(service=s, options=options) #Ya tenemos el bot creado y listo para hacer cositas.

    return bot


bot=configureBot()

bot.get(link_Sorteo) 
bot.find_element(By.XPATH,value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button').click()
time.sleep(4)


# bot.refresh()


