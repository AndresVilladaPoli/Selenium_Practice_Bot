from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

input = "Eldorado"
input1 = "Punta Cana"
input2 = "avianca"


service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
time.sleep(3)

bot.get("https://www.viajesexito.com")
time.sleep(4)
bot.get("https://www.viajesexito.com")


flightType = bot.find_element(By.XPATH, '//*[@id="paquetesTooltips"]/a')
flightType.click()
time.sleep(3)

Origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
Origin.click()
Origin1 = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveFrom_netactica_airhotel"]')
Origin1.send_keys(input)
Origin1.send_keys(Keys.ENTER)
time.sleep(3)


destination = bot.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
destination.click()
destination1 = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveTo_netactica_airhotel"]')
destination1.send_keys(input1)
destination1.send_keys(Keys.ENTER)
time.sleep(4)

openDates = bot.find_element(By.XPATH, '//*[@id="Date_netactica_air_hotel"]')
openDates.click()
time.sleep(5)
'''
departureDay = bot.find_element(By.XPATH, '//*[@id="Body"]/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[4]/div[2]/div[1]')
departureDay.click()
returnDate = bot.find_element(By.XPATH, '//*[@id="Body"]/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[4]/div[2]/div[1]')
returnDate.click()
acceptbutton = bot.find_element(By.XPATH, '//*[@id="Body"]/div[8]/div[2]/div[2]/div[3]/button[2]')
acceptbutton.click()
'''

lodging = bot.find_element(By.XPATH, '//*[@id="txtNumPassengersPaquetesComplete"]')
lodging.click()
lodging1 = bot.find_element(By.XPATH, '//*[@id="btbAddRoomtwopaquetes"]')
lodging1.click()
time.sleep(3)
lodging2 = bot.find_element(By.XPATH, '//*[@id="contentBgAutofocus"]')
lodging2.click()
time.sleep(3)

search = bot.find_element(By.XPATH, '//*[@id="sbm_netactica_airhotel"]')
search.click()
time.sleep(20)

all_windows = bot.window_handles
new_window = all_windows[-1]
bot.switch_to.window(new_window)
wait = WebDriverWait(bot, 10)
body = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
time.sleep(3)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)
body.send_keys(Keys.ARROW_DOWN)

price1 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[1]/div/div/div[2]/div/div[1]/div/p[1]').text
price2 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[2]/div/div/div[2]/div/div[1]/div/p[1]').text
price3 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[3]/div/div/div[2]/div/div[1]/div/p[1]').text
price4 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[4]/div/div/div[2]/div/div[1]/div/p[1]').text
price5 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[5]/div/div/div[2]/div/div[1]/div/p[1]').text
price6 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[6]/div/div/div[2]/div/div[1]/div/p[1]').text
price7 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[7]/div/div/div[2]/div/div[1]/div/p[1]').text
price8 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[8]/div/div/div[2]/div/div[1]/div/p[1]').text
price9 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[9]/div/div/div[2]/div/div[1]/div/p[1]').text
price10 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[10]/div/div/div[2]/div/div[1]/div/p[1]').text

print("")
print("*****************************************************************")
print("              The prices collected are the following:            ")
print("                                                                   ")
print("1."+price1)
print("2."+price2)
print("3."+price3)
print("4."+price4)
print("5."+price5)
print("6."+price6)
print("7."+price7)
print("8."+price8)
print("9."+price9)
print("10."+price10)
print("*****************************************************************")

advancedOptions = bot.find_element(By.XPATH, '//*[@id="aShowHideAdvanced"]')
advancedOptions.click()
airline = bot.find_element(By.XPATH, '//*[@id="txtAirlineCode"]')
airline.send_keys(input2)
airline.send_keys(Keys.ENTER)
button = bot.find_element(By.XPATH, '//*[@id="ulNewSearch"]/div[8]/input')
button.click()
time.sleep(10)

price1 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[1]/div/div/div[2]/div/div[1]/div/p[1]').text
price2 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[2]/div/div/div[2]/div/div[1]/div/p[1]').text
price3 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[3]/div/div/div[2]/div/div[1]/div/p[1]').text
price4 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[4]/div/div/div[2]/div/div[1]/div/p[1]').text
price5 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[5]/div/div/div[2]/div/div[1]/div/p[1]').text
price6 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[6]/div/div/div[2]/div/div[1]/div/p[1]').text
price7 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[7]/div/div/div[2]/div/div[1]/div/p[1]').text
price8 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[8]/div/div/div[2]/div/div[1]/div/p[1]').text
price9 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[9]/div/div/div[2]/div/div[1]/div/p[1]').text
price10 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[10]/div/div/div[2]/div/div[1]/div/p[1]').text

prices = []
for i in range(1, 11):  
    xpath = f'//*[@id="divAirResults"]/div[{i}]/div/div/div[2]/div/div[1]/div/p[1]'
    price = bot.find_element(By.XPATH, xpath).text
    prices.append(price)


file_path = 'AviancaPrices.txt'


with open(file_path, 'w', encoding='utf-8') as file:
    file.write('Avianca Prices\n')
    file.write('Flight: El Dorado (BOG) - Punta Cana (RD)\n')
    file.write('Date: 06/20/2024 - 06/27/2024 \n')
    for price in prices:
        file.write(f'{price}\n')

bot.save_screenshot("Screenshot.png")
time.sleep(7)
bot.quit()
