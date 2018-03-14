def napraw_plik():
    """
    Inputs:\n
    None\n
    ------------------\n
    Output:\n
    None, function is repairing file from serial port to be usefull for RNG
    """
    for i in range(20):
        plik=open('danemic/plik_mic'+str(i+1),'r')
        dane=plik.read()
        plik.close()
        dane=dane.split('\n')
        print len(dane)
        nowe=""
        for j in range(len(dane)):
            if '0' in dane[j]: nowe+="0"
            else: nowe+="1"
        #print nowe[:10],i
        plik.close()
        plik=open('danemic/plik_mic'+str(i+1)+".txt",'w')
        plik.write(nowe)
        plik.close()
        print "done"

if __name__ == '__main__':
    napraw_plik()
