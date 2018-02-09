def TestPojedynczegoBitu(i,nazwa,plik_out):
    print nazwa
    w=0
    plik_o1=open(plik_out+"2.txt",'a')
    plik_o0=open(plik_out+"1.txt",'a')
    plik_o1.write(str(i)+'\t')
    plik=open(nazwa,'r').read()
    for i in range(20000):
        if plik[i]=='1':w+=1
    plik_o1.write(str(w)+'\t')
    print str(w)
    if w>9725 and w<10275:
        plik_o0.write("T"+' ')
        return True
    plik_o0.write("F"+' ')
    return False

def decym(n):
    k,w=8,0
    for i in range(4):
        w+=int(n[i])*k
        k/=2
    return w

def TestPokerowy(nazwa,plik_out):
    plik_o1=open(plik_out+"2.txt",'a')
    plik_o0=open(plik_out+"1.txt",'a')
    plik=open(nazwa,'r').read()
    liczby=[]
    for i in range(0,20000,4):
        try:
            a=decym(plik[i]+plik[i+1]+plik[i+2]+plik[i+3])
            liczby.append(a)
        except:
            print g[i]+g[i+1]+g[i+2]+g[i+3]
            break
    w=0
    for i in range(16):
        w+=(liczby.count(i))**2
    w=(float(w)*16/5000)-5000
    plik_o1.write(str(w)+"\t")
    if w>2.16 and w<47.6:
        plik_o0.write("T"+' ')
        return True
    plik_o0.write("F"+' ')
    return False

def Serie(nazwa,plik_out):
    plik=open(nazwa,'r').read()
    serie={}
    ln=0
    for i in range(0,20000):
        if plik[i]=="0":
            ln+=1
            if i==19999:
                if ln in serie.keys(): serie[ln]+=1
                else: serie[ln]=1
                ln=0
            elif plik[i+1]=="1":
                if ln in serie.keys(): serie[ln]+=1
                else: serie[ln]=1
                ln=0
    return serie

akceptacja=[(2315,2685),(1114,1386),(527,723),(240,384),(103,209),(103,209)]

def TestSerii(nazwa,plik_out):
    plik_o0=open(plik_out+"1.txt",'a')
    plik_o1=open(plik_out+"2.txt",'a')
    serie=Serie(nazwa,plik_out)
    klucze=serie.keys()
    w=0
    out=""
    for i in range(1,6):
        if i in klucze:
            out+=str(serie[i])+"\t"
            if serie[i]>akceptacja[i][0] and serie[i]<akceptacja[i][1]:
                w+=1
            #print out
    #print out
    plik_o1.write(out)
    k=0
    for i in range(6,max(max(klucze)+1,7)):
        if i in klucze:
            k+=serie[i]
    plik_o1.write(str(k)+'\t')
    if k>103 and k<209: w+=1
    if w==6:
        plik_o0.write("T"+' ')
        return True
    plik_o0.write("F"+' ')
    return False

def TestNajdluzszejSerii(nazwa,plik_out):
    serie=Serie(nazwa,plik_out)
    plik_o0=open(plik_out+"1.txt",'a')
    plik_o1=open(plik_out+"2.txt",'a')
    plik_o1.write(str(max(serie.keys()))+'\n')
    if max(serie.keys())<26:
        plik_o0.write("T"+'\n')
        return True
    plik_o0.write("F"+'\n')
    return False

def generuj_wyniki(plik_in, plik_out, m):
    plik_o0=open(plik_out+"1.txt",'w')
    plik_o1=open(plik_out+"2.txt",'w')
    plik_o1.write("\tPojBit\tPok\tS1\tS2\tS3\tS4\tS5\tS>5\tNS\n")
    plik_o1.close()
    for i in range(m):
        TestPojedynczegoBitu(i+1,plik_in+str(i+1)+".txt",plik_out)
        TestPokerowy(plik_in+str(i+1)+".txt",plik_out)
        TestSerii(plik_in+str(i+1)+".txt",plik_out)
        TestNajdluzszejSerii(plik_in+str(i+1)+".txt",plik_out)
    

##generuj_wyniki("plik_mic","dane_mic",'\n',20)
##generuj_wyniki("plik_mic_xor","dane_mic_xor",'\n',10)
##generuj_wyniki("plik_mic_codrugi","dane_mic_codrugi",'\n',10)
##generuj_wyniki("plik_mic_korelacja","dane_mic_korelacja",'\n',10)
##generuj_wyniki("lfsr/LFSR","lfsr/lsfrout",1)
##generuj_wyniki('grailfsr/LFSRgame','grailfsr/LFSRgameout.txt',20)
##generuj_wyniki('lfsribbs/LFSRiBBS','lfsribbs/LFSRiBBSout.txt',1)
##generuj_wyniki('grailfsribbs/LFSRBBSgame','grailfsribbs/LFSRBBSgameout',20)
generuj_wyniki("wbudowane/gen_wb_pyt","wbudowane/gen_wb_pytout",20)
##generuj_wyniki("bbs/2BBSmb","bbs/2BBSmbout",1)
##generuj_wyniki("bbs/BBSxb","bbs/BBSxbout",1)
##generuj_wyniki("bbs/BBSsb","bbs/BBSsbout",1)
##
##plik_PB=open("testPB1.txt","w")
##plik_PB.write("1\n"*10250+"0\n"*9750)
##plik_PB.close()
##
##generuj_wyniki("testPB","testPBanaliza","\n",1)

##plik_PB=open("testS1.txt","w")
##plik_PB.write("1"*7+"0"*4+"1"*3+"0"*2+"1"*3+"0"*2+"1"*1+
##              "0"*1+"1"*1+"0"*19000+"1"*20000)
##plik_PB.close()
##print Serie("testS1.txt","w")
