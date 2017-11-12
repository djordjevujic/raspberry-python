import serial

ser = serial.Serial('/dev/ttyAMA0', baudrate=115200, timeout=2.0)  # open serial port

print('name: ' +ser.name)         # check which port was really used

while True:
    s = ser.read(10)
    print(s)

