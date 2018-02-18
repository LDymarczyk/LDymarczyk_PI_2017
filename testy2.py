import math
from scipy.special import gammaincc

def blocks_count(n, m, word):
    """
    Inputs:
    n - integer, length of word
    m - integer, length of block
    word - string of bytes
    --------------------------
    Output:
    dictionary, where keys are possible blocks and values are number of this blocks in word
    """
    lista = {}
    for i in range(pow(2, m)):
        e = bin(i)[2:]
        lista["0" * (m-len(e)) + e] = 0
    for i in range(n):
        a = word[i: i + m]
        lista[a] += 1
    return lista

def psi_calc(n, m, word):
    """
    Inputs:
    n - integer, length of word
    m - integer, length of block
    word - string of bytes
    --------------------------
    Output:
    float, value of psi function
    """
    word += word[ : m-1]
    val = blocks_count(n, m, word).values()
    ret = float(pow(2, m)) / n
    k = 0
    for i in range(pow(2, m)):
        k += pow(val[i], 2)
    return round(float(ret * k) - n, 4)

def PValues(n, m, word):
    """
    Inputs:
    n - integer, length of word
    m - integer, length of block
    word - string of bytes
    --------------------------
    Output:
    float, value of incomplete gamma function with suitable parameters
    """
    a = round(psi_calc(n, m, word) - psi_calc(n, m-1, word), 4)
    b = psi_calc(n, m, word) - 2 * psi_calc(n, m-1, word) + psi_calc(n, m-2, word)
    b = round(b, 4)
    return(gammaincc(pow(2, m-2), a / 2),gammaincc(pow(2, m - 3), b / 2))

def SerialTest(filein, n, m):
    """
    Inputs:
    n - integer, length of word
    m - integer, length of block
    filein - string of bytes
    --------------------------
    Output:
    Tuple of two float values
    """
    k = float(pow(2, m) / n)
    values = PValues(n, m, filein)
    t = "T"
    ret = ""
    for i in range(2):
        if values[i] < 0.01:
            t = "F"
        ret += str(round(values[i], 2)) + "\t"
    return (t, ret)

def Entropy(word, n, m):
    """
    Inputs:
    n - integer, length of word
    m - integer, length of block
    word - string of bytes
    --------------------------
    Output:
    folat, value of Entropy
    """
    word += word[ : m - 1]
    val = blocks_count(n, m, word).values()
    ret = 0
    for i in range(pow(2, m)):
        if val[i] != 0:
            ret += float(val[i]) / n * (math.log(float(val[i]) / n))
    return ret

def ApEntropyTest(filein, n, m):
    """
    Inputs:
    n - integer, length of word
    m - integer, length of block
    filein - string of bytes
    --------------------------
    Output:
    float, value of Entropy Test
    """
    chi = 2 * n * (math.log(2) - (Entropy(filein, n, m) - Entropy(filein, n, m + 1)))
    ret = round(gammaincc(pow(2, m - 1), chi / 2),2)
    t = "T"
    if ret < 0.01:
        t = "F"
    return (t, str(ret))

def SumBits(word, n):
    """
    Inputs:
    word - string of bytes
    n - integer, length of word
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

pi=[[0.5000, 0.2500, 0.1250, 0.0625, 0.0312, 0.0312],
    [0.7500, 0.0625, 0.0469, 0.0352, 0.0264, 0.0791],
    [0.8333, 0.0278, 0.0231, 0.0193, 0.0161, 0.0804],
    [0.8750, 0.0156, 0.0137, 0.0120, 0.0105, 0.0733]]

def CountSeries(sums, j):
    """
    Inputs:
    sums - List of intigers, sums S0...Sn, where n is number of bytes
    j - integer, number of sums
    --------------------------
    Output:
    List of 8 float values
    """
    numb = [-4, -3, -2, -1, 1, 2, 3, 4]
    ret = ""
    for i in range(8):
        numb_c = [0, 0, 0, 0, 0, 0]
        for m in range(j):
            v = sums[m].count(str(numb[i]))
            if v > 5: v = 5
            numb_c[v] += 1
            for g in range(v):
                sums[m] = sums[m].replace(str(numb[i]),"")
        s = 0
        for k in range(6):
            s += pow(numb_c[k]-j*pi[int(math.fabs(numb[i]))-1][k],2)/(j*pi[int(math.fabs(numb[i]))-1][k])
        ret += str(round(s, 2)) + "\t"
    return ret
                

def RanWTest(word, n):
    """
    Inputs:
    word - string of bytes
    n - integer, length of word
    --------------------------
    Output:
    List of 8 float values
    """
    sums = SumBits(word, n)
    sums = sums.split("0")
    for i in range(sums.count("")):
        sums.remove("")
    j = len(sums)
    ret = CountSeries(sums, j)
    t = "T"
    for i in range(8):
        if ret[i] < 0.01:
            t = "F"
    return (t, ret)

##print SerialTest("11010010011110010100",20,3)
##print SerialTest("0011011101",10,3)
##print SerialTest("1111111111",10,3)[0]<0.01
##print ApEntropyTest("0100110101",10,3)
print RanWTest("0110110101",10)
##print pow(1-3*0.5,2)/(3*0.5)+pow(1-3*0.25,2)/(3*0.25)+pow(0-3*0.125,2)/(3*0.125)+pow(1-3*0.0625,2)/(3*0.0625)+pow(0-3*0.0312,2)/(3*0.0312)+pow(0-3*0.0312,2)/(3*0.0312)
