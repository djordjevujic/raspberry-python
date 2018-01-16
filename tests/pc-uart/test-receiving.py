import serial


# convert string to hex
def to_hex(s):
    lst = []
    for ch in s:
        hv = hex(ch)
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)

    return lst

ser = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=0.5)  # open serial port
print('name: ' + ser.name)  # check which port was really used

while True:
    s = ser.read(10)
    print(to_hex(s))
