#from ctypes import windll, Structure, c_long, byref
from pseudolosowy_afiniczny import xor_byte, more_byte
from LFSRiBBS import lfsribbs_body
from lfsr import genLFSR
from math import ceil
from modify_points import biegunowy, chaos_map
import time

#class Punkt(Structure):
#    _fields_ = [("x", c_long), ("y", c_long)]

def PozycjaMyszy():
    """
    Inputs:\n
    None\n
    ------------------\n
    Output:\n
    list of integers, coordinates of mouse coursor
    """
    p = Punkt()
    windll.user32.GetCursorPos(byref(p))
    return [ p.x, p.y]

def MakePoints(n):
    """
    Inputs:\n
    n - integer, number of creating points\n
    ------------------\n
    Output:\n
    list of coordinades of mouse coursor
    """
    k = PozycjaMyszy()
    ret = [k]
    i, j = 0, 0
    prev = k
    while i < n:
        time.sleep(0.0005)
        k = PozycjaMyszy()
        j += 1
        if k != prev:
            i+=1
            ret.append(k)
            prev=k
    print j
    return ret

def SavePoints(k, n):
    """
    Inputs:\n
    n - integer, number of creating points\n
    k - integer, number of strings\n
    ------------------\n
    Output:\n
    None, but creates k files with points
    """
    for i in range(k):
        p=MakePoints(n)
        out=""
        for j in range(n):
            out+=str(p[j][0])+","+str(p[j][1])+";"
        f=open("Points"+str(i+1)+".txt", 'w')
        f.write(out)
        f.close()
        print "done"

def TakePoints(filename):
    """
    Inputs:\n
    filename - string, name of file with saved points\n
    ------------------\n
    Output:\n
    list of coordinates loaded from file
    """
    p=open(filename).read().split(";")
    out=[]
    for i in range(len(p)-1):
        cor=p[i].split(",")
        cor[0]=int(cor[0])
        cor[1]=int(cor[1])
        out.append(cor)
    return out
    
        

def MouseGen(n, points, filename):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    points - list of coordinates\n
    filename - string, name of file, destination for generated bytes\n
    ------------------\n
    Output:\n
    None, list of bytes made from coordinates uploaded to file
    """
    ret = ""
    for i in range(n):
        ret += xor_byte(1080*points[i][0] + points[i][1])
    f=open(filename, 'w')
    f.write(ret)
    f.close()
    print "done"

def MouseGenB(n, points, filename):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    points - list of coordinates\n
    filename - string, name of file, destination for generated bytes\n
    ------------------\n
    Output:\n
    None, list of bytes made from polar coordinates uploaded to file
    """
    points=biegunowy(points)
    ret = ""
    for i in range(n):
        ret += xor_byte(360*int(round(points[i][0])) + int(round(points[i][1])))
    f=open(filename, 'w')
    f.write(ret)
    f.close()
    print "done"

def MouseGenC(n, points, filename):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    points - list of coordinates\n
    filename - string, name of file, destination for generated bytes\n
    ------------------\n
    Output:\n
    None, list of bytes made from coordinates changed with map of chaos uploaded to file
    """
    points=chaos_map(points)
    ret = ""
    for i in range(n):
        ret += xor_byte(1024*int(round(points[i][0])) + int(round(points[i][1])))
    f=open(filename, 'w')
    f.write(ret)
    f.close()
    print "done"

def TRMGMultiple(n, filename, m):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    filename - string, prefix for name of file, destination for generated bytes\n
    m - integer, number of file we want to generate
    ------------------\n
    Output:\n
    None, calls function MouseGen m times
    """
    for i in range(m):
        points = TakePoints("pliki/Points"+str(i+1)+".txt")
        MouseGen(n, points, filename+str(i+1)+".txt")

def TRMGBMultiple(n, filename, m):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    filename - string, prefix for name of file, destination for generated bytes\n
    m - integer, number of file we want to generate
    ------------------\n
    Output:\n
    None, calls function MouseGenB m times
    """
    for i in range(m):
        points = TakePoints("pliki/Points"+str(i+1)+".txt")
        MouseGenB(n, points, filename+str(i+1)+".txt")

def TRMGCMultiple(n, filename, m):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    filename - string, prefix for name of file, destination for generated bytes\n
    m - integer, number of file we want to generate
    ------------------\n
    Output:\n
    None, calls function MouseGenC m times
    """
    for i in range(m):
        points = TakePoints("pliki/Points"+str(i+1)+".txt")
        MouseGenC(n, points, filename+str(i+1)+".txt")

def TRNGMouseBon(n, points, filename, j):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    points - list of coordinates\n
    filename - string, name of file, destination for generated bytes\n
    j - integer, number of seed's bytes\n 
    ------------------\n
    Output:\n
    None, list of bytes made from LFSR with seed created from coordinates uploaded to file
    """
    ret = ""
    for i in range(int(ceil(n/(2.0*j-1)))):
        ret += genLFSR(1080*points[i][0] + points[i][1], 2*j-1, j)
    f=open(filename, 'w')
    f.write(ret)
    f.close()
    print "done"

def TRNGMMouseBon(n, filename, j, m):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    filename - string, prefix for name of file, destination for generated bytes\n
    j - integer, number of seed's bytes\n 
    m - integer, number of file we want to generate
    ------------------\n
    Output:\n
    None, calls function TRNGMouseBon m times
    """
    for i in range(m):
        points = TakePoints("pliki/Points"+str(i+1)+".txt")
        TRNGMouseBon(n, points, filename+str(i+1)+".txt", j)

def TRNG2MouseBon(n, points, filename, j):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    points - list of coordinates\n
    filename - string, name of file, destination for generated bytes\n
    j - integer, number of seed's bytes\n 
    ------------------\n
    Output:\n
    None, list of bytes made from LFSR with seed created from coordinates changed by chaos map uploaded to file
    """
    points=chaos_map(points)
    ret = ""
    for i in range(int(ceil(n/(2.0*j-1)))):
        ret += genLFSR(1024*int(round(points[i][0])) + int(round(points[i][1])), 2*j-1, j)
    f=open(filename, 'w')
    f.write(ret)
    f.close()
    print "done"

def TRNGM2MouseBon(n, filename, j, m):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    filename - string, prefix for name of file, destination for generated bytes\n
    j - integer, number of seed's bytes\n 
    m - integer, number of file we want to generate
    ------------------\n
    Output:\n
    None, calls function TRNG2MouseBon m times
    """
    for i in range(m):
        points = TakePoints("pliki/Points"+str(i+1)+".txt")
        TRNG2MouseBon(n, points, filename+str(i+1)+".txt", j)

def TRNGMLB(n, points, filename, j):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    points - list of coordinates\n
    filename - string, name of file, destination for generated bytes\n
    j - integer, number of seed's bytes\n 
    ------------------\n
    Output:\n
    None, list of bytes made from LFSR connected with BBS with seed created from coordinates, uploaded to file
    """
    ret = ""
    for i in range(int(ceil(n/(2.0*j-1)))):
        ret += lfsribbs_body(1080*points[i][0] + points[i][1], 2*j-1, j)
    f=open(filename, 'w')
    f.write(ret)
    f.close()
    print "done"

def TRNGMMLB(n, filename, j, m):
    """
    Inputs:\n
    n - integer, number of bytes in the end file\n
    filename - string, prefix for name of file, destination for generated bytes\n
    j - integer, number of seed's bytes\n 
    m - integer, number of file we want to generate
    ------------------\n
    Output:\n
    None, calls function TRNGMouseBon m times
    """
    for i in range(m):
        points = TakePoints("pliki/Points"+str(i+1)+".txt")
        TRNGMLB(n, points, filename+str(i+1)+".txt", j)

if __name__ == '__main__':
##    TRMGMultiple(20000, "mouse/Mouse3Clear", 20)
##    TRMGBMultiple(20000, "mouse/Mouse1B", 20)
##    TRMGCMultiple(20000, "mouse/Mouse1C", 20)
    TRNGMMLB(20000, "mouse/Mouse1LB", 20, 20)
    TRNGM2MouseBon(20000, "mouse/Mouse2L", 20, 20)
##    TRNGMMouseBon(20000, "mouse/MouseL", 20, 20)
##    print MakePoints(200)
    #SavePoints(20,201)
    #print TakePoints("Points1.txt"), len(TakePoints("Points1.txt"))
