import smbus

bus = smbus.SMBus(1)
arduino_addr = 0x08

while True:
    try:
        entrada = int(input('Digite 1 para acender e 0 para apagar:'))
        
        if entrada == 1 or entrada == 0:
            bus.write_byte_data(arduino_addr, 0x00, entrada)
        else:
            print('O número digitado foi diferente de 0 ou 1. Encerrando...')
            break
    except ValueError:
        print('Valor inválido. Encerrando...')
        break
