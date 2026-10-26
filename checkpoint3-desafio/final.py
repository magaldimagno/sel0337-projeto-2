import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

# ID  da tag cadastrada
ID_AUTORIZADO = 771034125847

# Definição dos pinos do LED RGB
PINO_RED = 12 # Vermelho
PINO_GREEN = 13 # Verde
PINO_BLUE = 19 # Azul

# Configuração do modo de numeração dos pinos e desabilitação de avisos
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configuração dos pinos como saída
GPIO.setup(PINO_RED, GPIO.OUT)
GPIO.setup(PINO_GREEN, GPIO.OUT)
GPIO.setup(PINO_BLUE, GPIO.OUT)

# Inicialização do PWM a uma frequência de 100 Hz em cada pino
pwm_red = GPIO.PWM(PINO_RED, 100)
pwm_green = GPIO.PWM(PINO_GREEN, 100)
pwm_blue = GPIO.PWM(PINO_BLUE, 100)

# Inicia o PWM com duty cycle de 0% (LED desligado)
pwm_red.start(0)
pwm_green.start(0)
pwm_blue.start(0)

# Inicialização do leitor RFID
leitor = SimpleMFRC522()

# Função para definir a intensidade de cada cor (0 a 100%)
def definir_cor_pwm(r_duty, g_duty, b_duty):
    pwm_red.ChangeDutyCycle(r_duty)
    pwm_green.ChangeDutyCycle(g_duty)
    pwm_blue.ChangeDutyCycle(b_duty)

print("Sistema de acesso com PWM iniciado.")

try:
    while True:
        definir_cor_pwm(0, 0, 100) # Azul - Standby

        print("Aproxime a tag do leitor para leitura.")
        id, texto = leitor.read() # Lê a id e o texto da tag
        print("ID: {}\nTexto: {}".format(id, texto)) # Exibe as informações

        if id == ID_AUTORIZADO:
            print("Acesso autorizado!")
            definir_cor_pwm(0, 100, 0) # Verde
        else:
            print("Acesso negado!")
            definir_cor_pwm(100, 0, 0) # Vermelho

        sleep(3) # Aguarda 3 segundos antes de resetar a cor e ler novamente

except KeyboardInterrupt:
    # Para o PWM e limpa as configurações de GPIO ao encerrar
    pwm_red.stop()
    pwm_green.stop()
    pwm_blue.stop()
    GPIO.cleanup()
    print("\nPrograma interrompido pelo usuário.")