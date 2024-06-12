from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time

input = "Eldorado"
input1 = "Punta Cana"


service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
time.sleep(5)

bot.get("https://www.viajesexito.com")
time.sleep(4)
bot.get("https://www.viajesexito.com")


flightType = bot.find_element(By.XPATH, '//*[@id="paquetesTooltips"]/a')
time.sleep(3)
flightType.click()
time.sleep(2)

Origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
Origin.click()
Origin1 = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveFrom_netactica_airhotel"]')
Origin1.send_keys(input)
Origin1.send_keys(Keys.ENTER)
time.sleep(5)


destination = bot.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
destination.click()
destination1 = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveTo_netactica_airhotel"]')
destination1.send_keys(input1)
destination1.send_keys(Keys.ENTER)
time.sleep(3)
'''
departureDate = bot.find_element(By.XPATH, '//*[@id="Date_netactica_air_hotel"]')
departureDate.click()
time.sleep(3)
departureDate1 = bot.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[4]/div[2]/div[1]')
departureDate1.click()
'''
bot.execute_script("window.ScrollTo(0,1000)")
lodging = bot.find_element(By.XPATH, '//*[@id="txtNumPassengersPaquetesComplete"]')
lodging.click()
time.sleep(2)
lodging1 = bot.find_element(By.XPATH, '//*[@id="btbAddRoomtwopaquetes"]')
lodging1.click()
lodging2 = bot.find_element(By.XPATH, '//*[@id="btbClosePaxPopup"]')
lodging2.click()
time.sleep(2)

Price1 = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price2=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price3=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price4=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price5=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price6=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price7=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price8=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price9=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
Price10=bot.find_element(By.XPATH,  '//*[@id="divAirResults"]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text


print("")
print("The search prices are" + Price1 + Price2 + Price3 + Price4 + Price5 + Price6 + Price7 + Price8 + Price9 + Price10)