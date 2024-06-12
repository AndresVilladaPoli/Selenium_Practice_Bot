from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options 

import time

input = "El Dorado Bogota"
input1 = "Punta Cana"

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window
time.sleep(5)

bot.get("https://www.viajesexito.com")
time.sleep(3)

TipoVuelo = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]')
time.sleep(3)
TipoVuelo.click()
time.sleep(2)

Origen = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
Origen.click()
Origen.send_keys(input)
time.sleep(2)

Destino = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
Destino.click()
Destino.send_keys(input1)
time.sleep(2)

FechaSalida= bot.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div[1]')
FechaSalida.click()
time.sleep(2)

DiaSalida= bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[4]/div[2]/div[1]')
DiaSalida.click()
time.sleep(2)

DiaRegreso= bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[4]/div[2]/div[1]')
DiaRegreso.click()
time.sleep(2)

Habitacion1= bot.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
Habitacion1.click()
time.sleep(2)

AgregarHabitacion= bot.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]')
AgregarHabitacion.click()
time.sleep(2)

Habitacion2=bot.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
Habitacion2.click()
time.sleep(2)

Precio1 = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[4]/div/div[4]/div/div[2]/div/p[1]/span[2]').text
print(Precio1)


print("")
print("Los precios de la busqueda son" + Precio1)

