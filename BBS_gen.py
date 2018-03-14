from pseudolosowy_afiniczny import xor_byte, more_byte

def BBSgen_elem(x0, p, q):
    """
    Inputs:\n
    x0 - intiger number, seed for generator\n
    p,q - integers, constant for generator\n
    ------------------\n
    Output:\n
    List of strings - next integer for generator and byte generated on 3 ways
    """
    M = p*q
    x = (x0*x0)%M
    return [x, str(x%2), xor_byte(x), more_byte(x)]


def BBSgen_body(x, n, mode = 1):
    """
    Inputs:\n
    x - intiger number, seed for generator\n
    n - intiger, length of generating string of bytes\n
    mode - integer, 1 for bn - last byte, 2 for bn - xor all bytes, 3 for bn - compare number of bytes, 0 for receiving Xn\n
    ------------------\n
    Output:\n
    string, generated n bytes
    """
    begin = x
    out = ""
    for i in range(n):
        res = BBSgen_elem(x, 1287467, 4243067)
        x = res[0]
        if mode==1:
            out += res[1]
        elif mode==2:
            out += res[2]
        elif mode==3:
            out += res[3]
        else:
            out = x
        if x==begin:
            print i
    return out

def BBSgen(x, n, k, file_name, mode = 2):
    """
    Inputs:\n
    x - intiger number, seed for generator\n
    n - intiger, length of generating string of bytes\n
    k - string, number added at the end of file name\n
    file_name - string, name of creating file with result\n
    mode - integer, 1 for bn - last byte, 2 for bn - xor all bytes, 3 for bn - compare number of bytes, 0 for receiving Xn\n
    ------------------\n
    Output:\n
    None, but saving generated n bytes to file\n
    """
    out = BBSgen_body(x, n, mode)
    if mode==1:
        file_out = open(file_name+"sb"+k+".txt",'w')
    elif mode==2:
        file_out = open(file_name+"xb"+k+".txt",'w')
    else:
        file_out = open(file_name+"mb"+k+".txt",'w')
    file_out.write(str(out))
    file_out.close()
        

if __name__ == '__main__':
    for i in range(20):
        BBSgen(500*i+3, 20000, str(i+1), "bbs/BBS", 1)
        BBSgen(500*i+3, 20000, str(i+1), "bbs/BBS", 2)
        BBSgen(500*i+3, 20000, str(i+1), "bbs/BBS", 3)
