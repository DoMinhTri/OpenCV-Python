import serial
import time
import random

def initConnection(portNo, baudRate):
    try:
        ser = serial.Serial(portNo, baudRate)
        print("Connected")
        return ser
    except:
        print("Not connected")

def SendData(ser, data):
    try:    
        ser.write(data.encode())
        print(str(data))
    except:
        print("Data stranmission field")

if __name__ == "__main__":
    ser = initConnection("COM11",9600)
    while True:
        num = random.randint(0, 9)
        if num%2 == 0:
            sData = "A"
        else:
            sData = "a"
        sMessage = str(num) + " - " + sData
        SendData(ser,sData, sMessage)
        time.sleep(3)



