def xordane(dane1,dane2):
    """
    Inputs:\n
    dane1 - string with 20000 bytes\n
    dane2 - string with 20000 bytes\n
    ------------------\n
    Output:\n
    string with 20000 bytes made from dane1 and dane2 by using xor on bytes bi from both of strings
    """
    ret=''
    dane1=dane1.split('\n')
    dane2=dane2.split('\n')
    for i in range(20000):
        if dane1[i]==dane2[i]:
            ret+='1'
        else:
            ret+='0'
    return ret


def xorpliki(input1,input2,output):
    """
    Inputs:\n
    input1 - string, name of input file\n
    input2 - string, name of input file\n
    output - string, name of output file\n
    ------------------\n
    Output:\n
    None, but saving to output file string with 20000 bytes made from dane1 and dane2 by using xor on bytes bi from both of strings
    """
    plik1=open(input1,'r').read()
    plik2=open(input2,'r').read()
    dane=xordane(plik1,plik2)
    plik_o=open(output,'w')
    plik_o.write(dane)
    plik_o.close()
    return "done"
    


def xorowanie(plik_in, plik_out):
    """
    Inputs:\n
    plik_in - string, prefix for name of input file\n
    plik_out - string, prefix for name of input file\n
    ------------------\n
    Output:\n
    None
    """
    for i in range(1,21,2):
        xorpliki(plik_in+str(i)+".txt",plik_in+str(i+1)+".txt",
                 plik_out+str((i+1)/2)+".txt")


if __name__ == '__main__':
    xorowanie("danemic/plik_mic","mic_xor/plik_mic_xor")
