import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)
leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para leitura.")

while True:
    id, texto = leitor.read() # lê a id e o texto da tag
    print("ID: {}\nTexto: {}".format(id, texto)) # exibe as informações
    sleep(3) # aguarda 3 segundos para nova leitura