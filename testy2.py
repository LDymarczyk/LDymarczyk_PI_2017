import math

def blocks_count(n, m, word):
    """
    Inputs:\n
    n - integer, length of word\n
    m - integer, length of block\n
    word - string of bytes\n
    --------------------------\n
    Output:\n
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
    Inputs:\n
    n - integer, length of word\n
    m - integer, length of block\n
    word - string of bytes\n
    --------------------------\n
    Output:\n
    float, value of psi function
    """
    word += word[ : m-1]
    val = blocks_count(n, m, word).values()
    ret = float(pow(2, m)) / n
    k = 0
    for i in range(pow(2, m)):
        k += pow(val[i], 2)
    return round(float(ret * k) - n, 4)


def SerialTest(filein, n, m):
    """
    Inputs:\n
    n - integer, length of word\n
    m - integer, length of block\n
    filein - string of bytes\n
    --------------------------\n
    Output:\n
    Tuple of two float values
    """
    a = round(psi_calc(n, m, filein) - psi_calc(n, m-1, filein), 4)
    b = psi_calc(n, m, filein) - 2 * psi_calc(n, m-1, filein) + psi_calc(n, m-2, filein)
    b = round(b, 4)
    values = [a, b]
    t = "T"
    ret = ""
    if values[0] < 0.02 or values[0] > 13.28:
        t = "F"
    if values[1] < 0.01 or values[1] > 9.2:
        t = "F"
    ret += str(round(values[0], 2)).replace('.',',') + "\t" +  str(round(values[1], 2)).replace('.',',') + "\t"
    return (t, ret)

def Entropy(word, n, m):
    """
    Inputs:\n
    n - integer, length of word\n
    m - integer, length of block\n
    word - string of bytes\n
    --------------------------\n
    Output:\n
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
    Inputs:\n
    n - integer, length of word\n
    m - integer, length of block\n
    filein - string of bytes\n
    --------------------------\n
    Output:\n
    float, value of Entropy Test
    """
    ret = Entropy(filein, n, m) - Entropy(filein, n, m + 1)
    t = "T"
    if ret < 0.692644925 or ret > 0.6931060175:
        t = "F"
    return (t, str(ret).replace('.',','))


##print SerialTest("11010010011110010100",20,3)
##print SerialTest("0011011101",10,3)
##print SerialTest("1111111111",10,3)[0]<0.01
##print ApEntropyTest("0100110101",10,3)
##print RanWTest("0110110101",10)
##print pow(1-3*0.5,2)/(3*0.5)+pow(1-3*0.25,2)/(3*0.25)+pow(0-3*0.125,2)/(3*0.125)+pow(1-3*0.0625,2)/(3*0.0625)+pow(0-3*0.0312,2)/(3*0.0312)+pow(0-3*0.0312,2)/(3*0.0312)
