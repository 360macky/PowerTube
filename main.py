import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("AutoMP3")
print("Disponible para Chrome Versión 78+ | Creado con YtMp3.cc")
url = str(input("Ingresa la URL del vídeo en YouTube: "))

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://ytmp3.cc/')
input_url = browser.find_element_by_id('input')
input_url.send_keys(url)
input_url.send_keys(Keys.ENTER)
time.sleep(2)
download_button = browser.find_element_by_link_text('Download')
download_button.click()
print("Vídeo descargado exitosamente")
