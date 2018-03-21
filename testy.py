from testy2 import SerialTest, ApEntropyTest

def TestPojedynczegoBitu(plik):
    """
    Inputs:\n
    plik - string of 20.000 bytes\n
    ------------------\n
    Output:\n
    Tuple of strings:\n
    first element is boolean value "T" if test was succesfull "F" if test failed
    second element is value of the Monobit Test
    """
    w = 0
    for i in range(20000):
        if plik[i] == '1': w += 1
    if w>9818 and w<10182:
        return ("T", str(w))
    return ("F",str(w))

def decym(n):
    k, w= 8, 0
    for i in range(4):
        w += int(n[i]) * k
        k /= 2
    return w

def TestPokerowy(plik):
    """
    Inputs:\n
    plik - string of 20.000 bytes\n
    ------------------\n
    Output:\n
    Tuple of strings:\n
    first element is boolean value "T" if test was succesfull "F" if test failed
    second element is value of the Frequency Test within a Block
    """
    liczby = []
    for i in range(0, 20000, 4):
        try:
            a = decym(plik[i] + plik[i+1] + plik[i+2] + plik[i+3])
            liczby.append(a)
        except:
            print g[i] + g[i+1] + g[i+2] + g[i+3]
            break
    w = 0
    for i in range(16):
        w += (liczby.count(i)) ** 2
    w = (float(w) * 16 / 5000) - 5000
    if w > 5.23 and w < 30.58:
        return ("T", str(w).replace('.',','))
    return ("F" , str(w).replace('.',','))

def Serie(plik):
    """
    Inputs:\n
    plik - string of 20.000 bytes\n
    ------------------\n
    Output:\n
    dictionary where keys are lenhgts of runs and values are number of runs
    """
    serie = {}
    ln = 0
    for i in range(0, 20000):
        if plik[i] == "0":
            ln += 1
            if i == 19999:
                if ln in serie.keys(): serie[ln] += 1
                else: serie[ln] = 1
                ln=0
            elif plik[i+1] == "1":
                if ln in serie.keys(): serie[ln] += 1
                else: serie[ln] = 1
                ln = 0
    return serie

akceptacja = [(2315,2685), (1114,1386), (527,723), (240,384), (103,209), (103,209)]

def TestSerii(plik):
    """
    Inputs:\n
    plik - string of 20.000 bytes\n
    ------------------\n
    Output:\n
    Tuple of strings:\n
    first element is boolean value "T" if test was succesfull "F" if test failed
    second element is value of the Runs Test
    """
    serie = Serie(plik)
    out = ""
    k = sum(serie.values())
    out += str(k)
    if k > 4909 and k < 5091:
        return ("T", str(out))
    return ("F", str(out))

def TestNajdluzszejSerii(nazwa):
    """
    Inputs:\n
    plik - string of 20.000 bytes\n
    ------------------\n
    Output:\n
    Tuple of strings:\n
    first element is boolean value "T" if test was succesfull "F" if test failed
    second element is value of the Test for the Longest Run
    """
    serie = Serie(nazwa)
    w = (str(max(serie.keys())))
    if max(serie.keys()) < 20 and max(serie.keys()) > 11:
        return ("T", str(w))
    return ("F", str(w))

def generuj_wyniki(plik_in, plik_out, m):
    """
    Inputs:\n
    plik_in - string, name of the file with generated bytes, only the prefix without sumple number\n
    plik_out - string, name of final file, where will be save the results of tests\n
    m - number of sumples\n
    ------------------\n
    Output:\n
    None
    """
    p1 = "\tPojBit\tPok\tTS\tNS\tST1\tST2\tApEn\n"
    p2 = "\tPojBit\tPok\tTS\tNS\tST\tApEn\n"
    for i in range(m):
        pi = open(plik_in+str(i+1)+".txt", "r").read()
        res1 = TestPojedynczegoBitu(pi)
        res2 = TestPokerowy(pi)
        res3 = TestSerii(pi)
        res4 = TestNajdluzszejSerii(pi)
        res5 = SerialTest(pi, 20000, 3)
        res6 = ApEntropyTest(pi, 20000,3)
        p2 += str(i+1) + "\t" + res1[0] + "\t" + res2[0] + "\t" + res3[0] + "\t" + res4[0] + "\t" + res5[0] + "\t" + res6[0] + "\n"
        p1 += str(i+1) + "\t" + res1[1] + "\t" + res2[1] + "\t" + res3[1] + "\t" + res4[1] + "\t" + res5[1] + res6[1] + "\n"
    plik_o0 = open(plik_out+"1.txt", 'w')
    plik_o1 = open(plik_out+"2.txt", 'w')
    plik_o0.write(p1)
    plik_o1.write(p2)
    plik_o0.close()
    plik_o1.close()
    

if __name__ == '__main__':
    
##    generuj_wyniki("danemic/plik_mic","danemic/plik_mic_out",20)
##    generuj_wyniki("mic_xor/plik_mic_xor","mic_xor/dane_mic_xor",10)
##    generuj_wyniki("mic_codrugi/plik_mic_codrugi","mic_codrugi/dane_mic_codrugi",10)

##    generuj_wyniki("trng/TRNG","trng/TRNG_out",10)

##    generuj_wyniki("lfsribbs/LFSRiBBS","lfsribbs/LFSRiBBSout",20)
##    generuj_wyniki("afiniczny/af_more","afiniczny/af_more_out",20)
    generuj_wyniki("afiniczny/af_xor","afiniczny/af_xor_out",20)
##        
    ##generuj_wyniki("lfsr/LFSR","lfsr/lsfrout",1)
        
    ##generuj_wyniki("mouse/Mouse1Clear","mouse/zMouse1out",20)
    ##generuj_wyniki("mouse/Mouse2Clear","mouse/zMouse2out",20)
    ##generuj_wyniki("mouse/Mouse3Clear","mouse/zMouse3out",20)
    ##generuj_wyniki("mouse/Mouse2L","mouse/zMouse2Lout",20)
    ##generuj_wyniki("mouse/Mouse1LB","mouse/zMouse1LBout",20)
    ##generuj_wyniki("mouse/MouseL","mouse/zMouse1Lout",20)
    ##generuj_wyniki("mouse/Mouse1B","mouse/zMouse1Bout",20)
    ##generuj_wyniki("mouse/Mouse1LB","mouse/zMouse1LBout",20)
    ##generuj_wyniki("mouse/Mouse1C","mouse/zMouse1Cout",20)
        
    ##generuj_wyniki("bbs/BBSmb","bbs/BBSmbout",20)
    ##generuj_wyniki("bbs/BBSxb","bbs/BBSxbout",20)
    ##generuj_wyniki("bbs/BBSsb","bbs/BBSsbout",20)
