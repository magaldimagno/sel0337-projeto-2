import smbus
import time

bus = smbus.SMBus(1)
arduino_addr = 0x08

while True:
    try:
        bloco = bus.read_i2c_block_data(arduino_addr, 0x00, 2)

        byte_alto = bloco[0]
        byte_baixo = bloco[1]

        valor_reconstruido = (byte_alto << 8) | byte_baixo

        print(f"Valor recebido: {valor_reconstruido}")

        time.sleep(0.5)
    except Exception as e:
        print(f"Erro na comunicação: {e}")
        break
