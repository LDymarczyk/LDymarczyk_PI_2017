from MouseGen import MakePoints
from lfsr import genLFSR
from BBS_gen import BBSgen_body
from math import ceil, floor
from modify_points import chaos_map

def BintoInt(x):
    """
    Inputs:\n
    x - string of bytes\n
    ------------------\n
    Output:\n
    integer x
    """
    k = 1
    out = 0
    for i in range(len(x)-1, -1, -1):
        out += k * int(x[i])
        k *= 2
    return out
    

def TRNGalg(n, j, k):
    """
    Inputs:\n
    n - intiger, length of generated string of bytes\n
    j - integer, length of cycle (PRNG will make j bytes from one seed)\n
    k - integer, number of bytes in register\n
    where j < 2*k, k < n\n
    ------------------\n
    Output:\n
    string, generated n bytes
    """
    m = int(ceil(float(n)/j))
    points = chaos_map(MakePoints(m))
    out = ""
    for i in range(m):
        x = int(round(points[i][0] * 1024 + points[i][1]))
        it = 0
        while it < j:
            xb = BBSgen_body(x, 1)
            xl = genLFSR(x, 1, k)
            if xb != xl:
                out += xb
                it+=1
            x = BBSgen_body(x, 1, 0)
    return out
    
        
        
def TRNG(m, k = 1):
    """
    Inputs:\n
    m - intiger, 2^m will be upper range of generated values\n
    k - integer, number of generated values\n
    m * k < 20.001\n
    ------------------\n
    Output:\n
    list of x integers
    """
    print ("=========================\nProsimy o poruszanie kursorem\n=========================")
    l = []
    bs = TRNGalg(20000, 25, 20)
    if k == 1:
        print ("=========================\nDziekujemy\n=========================")
        return BintoInt(bs[:m])
    for i in range(k):
        x = BintoInt(bs[:m])
        l.append(x)
        bs = bs[m:]
    print ("=========================\nDziekujemy\n=========================")
    return l

if __name__ == '__main__':
##    for i in range(10):
##        b = TRNGalg(20000, 25, 20)
##        print i
##        f = open("trng/TRNG"+str(i+1)+".txt","w")
##        f.write(b)
##        f.close()
##    print TRNG(4) ##Generuje liczbe z zakresu <0, 2^m-1>
    print (TRNG(10, 50)) ## Generuje 50 liczb z zakresu <0, 2^m-1>
