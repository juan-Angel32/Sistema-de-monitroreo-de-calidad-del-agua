#Sensor De Turbidez Analógico
from machine import ADC 
import time 
turbidity_pin = 34  # Ajusta según el pin en el que esté conectado tu sensor 
adc = ADC(Pin(turbidity_pin)) 
adc.width(ADC.WIDTH_12BIT)  # Configura la resolución a 12 bits (0-4095) 
adc.atten(ADC.ATTN_11DB)  # Configura la atenuación a 11 dB para un rango de 0-3.3V 
while True: 
turbidity_value = adc.read() 
print("Turbidity:", turbidity_value) 
t
 ime.sleep_ms(100)