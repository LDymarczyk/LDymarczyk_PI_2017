from lfsr import LFSR_body, genLFSR
from BBS_gen import BBSgen_body

def lfsribbs_body(x0,n,k):
    """
    Inputs:\n
    x0 - intiger number, seed for generator\n
    n - intiger, length of generating string of bytes\n
    k - integer, number of bytes in register\n
    ------------------
    Output:\n
    string, generated n bytes\n
    """
    out=""
    i=0
    while i<n:
        x1=genLFSR(x0,1,k)
        x2=BBSgen_body (x0, 1)
        if x1!=x2:
            out+=x2
            i+=1
        x0=BBSgen_body (x0, 1,0)
    #print i
    return out

if __name__ == '__main__':
    x=201
    for i in range(20):
        x0=lfsribbs_body(i*x+7,20000,15)
        fileout=open("lfsribbs/LFSRiBBS"+str(i+1)+".txt",'w')
        fileout.write(x0)
        fileout.close()
