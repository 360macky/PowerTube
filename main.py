import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("AutoMP3")
print("Disponible para Chrome Versión 78+ | Creado con YtMp3.cc")
url = str(input("Ingresa la URL del vídeo en YouTube: "))
print("¿Deseas descargar audio o vídeo?")
print("a -> Audio")
print("v -> Video")
type_download = str(input("Escribe (a/v): "))
type_download = type_download.capitalize()

if type_download == 'A':
    print("Descargando en formato de audio...")
elif type_download == 'V':
    print("Descargando en formato de video...")
else:
    print("Descargando en formato audio por defecto...")
    type_download = 'A'

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://ytmp3.cc/')
input_url = browser.find_element_by_id('input')

mp3_option = browser.find_element_by_id('mp3')
mp4_option = browser.find_element_by_id('mp4')

if type_download == 'A':
    mp3_option.click()
else:
    mp4_option.click()

input_url.send_keys(url)
input_url.send_keys(Keys.ENTER)
time.sleep(6)
download_button = browser.find_element_by_link_text('Download')
title_download = browser.find_element_by_id('title').text
download_button.click()

print("'" + title_download + "' descargando...")

if type_download == 'A':
    print("Audio descargando satisfactoriamente")
else:
    print("Video descargando satisfactoriamente")

