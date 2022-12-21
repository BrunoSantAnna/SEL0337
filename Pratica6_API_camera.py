import json
import requests
import pprint

from picamera import PiCamera
from time import sleep

#Camera
camera = PiCamera() # inicializa a câmera

camera.resolution = (2592, 1944) # seta a resolução da câmera para 2592x1944
camera.framerate = 15 # seta o framerate para 15 fps

camera.start_preview()
camera.annotate_text_size = 50 # seta o tamanho do texto na imagem
camera.annotate_text = "11819507 - 11800991" # escreve na imagem o texto entre aspas
sleep(5)
camera.capture('/home/sel/Bruno_e_WIll/foto.jpg')
camera.stop_preview()


#Dados meteorológicos
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
ID = '966583'
url = url + ID # definindo a url do site onde as informações meteorológicas da base desejada estão

info = get(url).json()['items'] # faz a requisição e transforma os dados recebidos em um dicionário, pegando apenas a coluna 'items'
pprint(info)
