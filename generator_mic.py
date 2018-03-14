#import serial, string
from time import sleep

def generuj_plik(nazwa_pliku):
    """
    Inputs:\n
    nazwa_pliku - string, name of creating file with result\n
    ------------------\n
    Output:\n
    None, but saving generated n bytes to file, function is related with arduino by serial port
    """
    ser = serial.Serial('COM4', 9600,timeout=1)
    i=0
    plik = open(nazwa_pliku,'w')
    schowek=""
    while i<20001:
        i+=1
        sleep(0.001)
        output = ser.readline()
        schowek+=output
    plik.write(schowek)
    plik.close()
    print "done"

if __name__ == '__main__':
    for i in range(20):
        generuj_plik("plik_mic"+str(i+1))
