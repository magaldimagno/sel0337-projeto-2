import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False) # desabilita os avisos
leitor = SimpleMFRC522() # cria o objeto "leitor"

# Altere para o seu número USP ou a combinação da dupla
texto = "SEU_NUMERO_USP_AQUI" 

print("Aproxime a tag do leitor para gravar.") 
leitor.write(texto) # realiza a gravação
print("Concluído!") 