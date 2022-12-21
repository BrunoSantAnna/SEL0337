# SEL0337

O projeto consiste em duas partes, uma que realiza o acesso à câmera à paritr da rasp e tira uma foto. A outra acessa um banco de dados de estações climáticas e recebe os dados de uma estação localizada na UFPR.

## Acesso à câmera:

Para acessar a câmera conectada à raspberry pi, foi utilizada a biblioteca picamera, uma biblioteca criada pela própria RaspberryPi Foundation para acesso e controle do módulo de câmera utilizando Python.
```Python
from picamera import PiCamera
```

Com essa biblioteca, foi necessário inicializar a câmera e definir seus parâmetros de resolução e _framerate_.

```Python
camera = PiCamera() # inicializa a câmera

camera.resolution = (2592, 1944) # seta a resolução da câmera para 2592x1944
camera.framerate = 15 # seta o framerate para 15 fps
```

Em seguida, deve-se usar o método `preview` para que a câmera começe a captar imagens e utilizar os comandos de annotation para escrever o texto na imagem.

```Python
camera.start_preview() # câmera começa a captar imagens

camera.annotate_text_size = 50 # seta o tamanho do texto na imagem
camera.annotate_text = "11819507 - 11800991" # escreve na imagem o texto entre aspas
```

Após isso, basta tirar a foto. A função `sleep` é utilizada para dar estabilidade à imagem, fazendo com que a foto não seja tirada exatamente no momento da execução do programa, que é bastante rápido. Essa função é importada da biblioteca `time`.

```Python
sleep(5) # pausa a execução do programa por 5 segundos
camera.capture('/home/sel/Bruno_e_WIll/foto.jpg') # tira a foto e a salva na pasta desejada
camera.stop_preview() # faz com que a câmera pare de captar imagens
```


## Uso da API para acesso ao banco de dados meteorológico

A segunda parte da prática consistiu em utilizar um script em pytho que é capaz de pegar informações que um site devolve utilizando o formato JSON e printá-los na tela. Em primeiro lugar, foi  necessário importar as bibliotecas `json` e a `requests`.

```Python
import json
import requests
```

Para saber onde buscar as informações, foi necessário fornecer ao programa a URL do site onde estão presentes as informações climáticas e o ID da base desejada.

```Python
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
ID = '966583'
url = url + ID # definindo a url do site onde as informações meteorológicas da base desejada estão
```

Após isso, as informações foram acessadas utilizando a função `get`, que irá enviar uma requisição de dados ao site e receber essas informações. Como a informação é passada com o formato JSON, é preciso utilizar o método `.json()` da biblioteca `requests` para transformar os dados em um dicionário.

```Python
info = get(url).json()['items'] # faz a requisição e transforma os dados recebidos em um dicionário, pegando apenas a coluna 'items'
pprint(info)
```
