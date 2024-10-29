#codigo para Liquid PH 0-14 sensor de ph 
from machine import ADC 
import time 
pot_pin = 34  # Puedes cambiar esto según el pin en el que esté conectado tu sensor 
adc = ADC(Pin(pot_pin)) 
adc.width(ADC.WIDTH_12BIT)  # Configura la resolución a 12 bits (0-4095) 
adc.atten(ADC.ATTN_11DB)  # Configura la atenuación a 11 dB para un rango de 0-3.3V 
while True: 
value = adc.read() 
print(value, "|", end=" ") 
voltage = value * (3.3 / 4095.0) 
ph = 3.3 * voltage  # Ajusta esta ecuación según las especificaciones de tu sensor 
print(ph) 
time.sleep_ms(500) 