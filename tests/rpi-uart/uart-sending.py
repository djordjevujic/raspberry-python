import serial
import time

s = serial.Serial('/dev/ttyAMA0', baudrate=115200, timeout=2.0)  # open serial port

print('name: ' +s.name)         # check which port was really used

while True:
    s.write(b'hello')     # write a string
    time.sleep(1)

