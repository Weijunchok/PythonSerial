from serial import Serial
from threading import Thread
import time
commPort='COM42'
ser = ""
def readSerial():
    global ser
    while True:
        if ser.is_open and ser.inWaiting()>0:
            recestr = ser.readline().decode()
            print(recestr)
def run():
    global ser
    try:
        ser=Serial(commPort,baudrate=9600, timeout=0.01)
        t = Thread(target=readSerial, name='readserial')                   # New receiving thread
        t.setDaemon(True)
        t.start()
    except:
        print("SERIAL CONNECTION FAILED!!!")
    i = 0
    while True:
        i = i + 1
        ser.write(str(i).encode())
        time.sleep(1)
        pass
if __name__ == "__main__":
    run()