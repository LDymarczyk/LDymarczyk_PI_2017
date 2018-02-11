import math
import mpmath
import scipy
from scipy.special import gammaincc

def blocks_count(n,m,word):
    lista={}
    for i in range(pow(2,m)):
        e=bin(i)[2:]
        lista["0"*(m-len(e))+e]=0
    #print len(word)
    for i in range(n):
        a=word[i:i+m]
##        print a
        lista[a]+=1
    return lista

def psi_calc(n,m,word):
    word+=word[:m-1]
    print word
    val=blocks_count(n,m,word).values()
    #print val
    ret=float(pow(2,m))/n
    k=0
    for i in range(pow(2,m)):
        k+=pow(val[i],2)
    return round(float(ret*k)-n,4)

def PValues(n,m,word):
    a=round(psi_calc(n,m,word)-psi_calc(n,m-1,word),4)
    b=psi_calc(n,m,word)-2*psi_calc(n,m-1,word)+psi_calc(n,m-2,word)
    b=round(b,4)
    return(gammaincc(pow(2,m-2),a/2),gammaincc(pow(2,m-3),b/2))

def SerialTest(filein,n,m):
    #plik=open(filein,'r').read()
    #sigma1=blocks_count(n,m,filein)
    #sigma2=blocks_count(n,m-1,filein)
    #print sigma1, sigma2
    k=float(pow(2,m)/n)
    return PValues(n,m,filein)

def Entropy(word,n,m):
    word+=word[:m-1]
##    print word
    val=blocks_count(n,m,word).values()
##    print val
    ret=0
    for i in range(pow(2,m)):
        if val[i]!=0:
##            print float(val[i])/n,(math.log(float(val[i])/n))
            ret+=float(val[i])/n*(math.log(float(val[i])/n))
    return ret

def ApEntropyTest(filein,n,m):
##    print Entropy(filein,n,m)-Entropy(filein,n,m+1),math.log(2)
    chi=2*n*(math.log(2)-(Entropy(filein,n,m)-Entropy(filein,n,m+1)))
    return gammaincc(pow(2,m-1),chi/2)

def SumBits(word,n):
    """
    Inputs:
    word - string of bits
    n - integer, leght of word
    --------------------------
    Output:
    List of sums S0...Sn
    """
    s=0
    ret="0"
    for i in range(n):
        s+=2*int(word[i])-1
        ret+=str(s)
    ret+="0"
    return ret

pi=[[0.5,0.2500,0.1250,0.0625,0.0312,0.0312],
    [0.75,0.0625,0.0469,0.0352,0.0264,0.0791],
    [0.8333,0.0278,0.0231,0.0193,0.0161,0.0804],
    [0.875,0.0156,0.0137,0.012,0.0105,0.0733]]

def CountSeries(sums,j):
    numb=[-4,-3,-2,-1,1,2,3,4]
    ret=[]
    for i in range(8):
        numb_c=[0,0,0,0,0,0]
        for m in range(j):
            v=sums[m].count(str(numb[i]))
            if v>5: v=5
            numb_c[v]+=1
            for g in range(v):
                sums[m]=sums[m].replace(str(numb[i]),"")
##            print numb[i], sums[m], v, numb_c
##        print numb_c
        s=0
        for k in range(6):
            print numb_c[k],j,pi[int(math.fabs(numb[i]))-1][k],j,pi[int(math.fabs(numb[i]))-1][k]
            s+=pow(numb_c[k]-j*pi[int(math.fabs(numb[i]))-1][k],2)/(j*pi[int(math.fabs(numb[i]))-1][k])
        print s
        ret.append(s)
    return ret
                

def RanW(word,n):
    sums=SumBits(word,n)
    sums=sums.split("0")
    for i in range(sums.count("")):
        sums.remove("")
    j=len(sums)
    ret=CountSeries(sums,j)
    return ret

##print SerialTest("11010010011110010100",20,3)
##print SerialTest("0011011101",10,3)
##print SerialTest("1111111111",10,3)[0]<0.01
##print ApEntropyTest("0100110101",10,3)
print RanW("0110110101",10)
##print pow(1-3*0.5,2)/(3*0.5)+pow(1-3*0.25,2)/(3*0.25)+pow(0-3*0.125,2)/(3*0.125)+pow(1-3*0.0625,2)/(3*0.0625)+pow(0-3*0.0312,2)/(3*0.0312)+pow(0-3*0.0312,2)/(3*0.0312)
