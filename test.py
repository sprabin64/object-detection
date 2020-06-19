import serial

def lightBulb():
    #ser = serial.Serial('/dev/ttyUSB0', 9600)
    data = '1'
    #ser.write(data.encode())
def turnOffBulb():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
