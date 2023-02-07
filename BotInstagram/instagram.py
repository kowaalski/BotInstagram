from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait #Se espera a actuar hasta que toda la pagina esta cargada.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from termcolor import colored, cprint
import random
import json

#LIMITE DIARIO 1440 COMENTARIOS, MAXIMO 60/HORA COMO MINIMO 1/MINUTO

def readProfile():
    
    with open("config.json", 'r') as archivo:
        data= json.load(archivo)
        user = data['user']
        password = data['password']
        link_raffle = data['link_raffle']
    
    return user,password,link_raffle


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


def log_in(user,password):
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


def readFollowers():
    newList=list()
    f = open('followers.txt', 'r')
    followers = f.readlines()
    f.close()
    cprint('Followers list charged', 'green',attrs=['bold','blink'])
    for i in followers:
        newList.append('@'+i.replace('\n',''))
    return newList


def delayCommenting():
    time.sleep(random.uniform(70, 120)) #Entre 1 min con 10s y 2 minutos


def postingComments():
    contRefresco=0
    
    for user in followersList:
        contRefresco=contRefresco+1
        if (contRefresco%5)==0: #Cada 5 usuarios metidos refresca la pagina.
            try:
                bot.refresh()
                time.sleep(20)
            except:
                pass
        
        #Primeros hacemos click en el form anterior a texarea, para que cargue en la pagina bien el text area y podamos meter datos con send keys
        WebDriverWait(bot, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form')))\
            .click()
      
        WebDriverWait(bot, 10)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')))\
            .send_keys(user)

        delay()

        #Enviamos comentario
        bot.find_element(By.XPATH,value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div').click()
        
        print('\n****************************************************************************************************************************')
        
        userColored=colored(user.center(25),'green', attrs=['reverse', 'blink'])
        addedColored=colored(' ADDED TO RAFFLE','green')
        print(userColored+addedColored)

        with open('usersAded.txt', 'a') as f:
            f.write(user+'\n')
        

        delayCommenting() #En el mejor de los casos en el que brinda el delay el menor tiempo de espera, obtenemos 51,42 comentarios, respetamos asi el limite de 60 por hora.
    
    cprint("ALL FOLLOWERS ADDED TO RAFFLE","yellow")  


if __name__ == '__main__':
    
    user,password,link_raffle=readProfile()
    bot = configureBot()

    # Inicializamos el navegador
    bot.get('https://www.instagram.com/')
    time.sleep(7)
    
    log_in(user,password)
    followersList=readFollowers()
    time.sleep(10)
    
    #Para abrir una pestaña nueva
    bot.execute_script('window.open('');') 
    bot.switch_to.window(bot.window_handles[1]) 
    bot.get(link_raffle) 
    
    time.sleep(4)
    postingComments()
    


        



        
        


    





