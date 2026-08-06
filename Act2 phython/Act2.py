import serial
import time

print("Conectando al Arduino...")
arduino = serial.Serial('COM6', 9600, timeout = 3.0)
print("Conectado al Arduino.")

time.sleep(2) 

while True:
    arduino.write("r".encode())
    val = arduino.readline().strip()
    
    if not val:
        continue
    
    try:
        val_limpio = val.decode('utf-8') 
        val = int(val_limpio)
        print(val)
    except (ValueError, UnicodeDecodeError):
        print("Dato corrupto recibido, reintentando...")
        
    time.sleep(0.5)