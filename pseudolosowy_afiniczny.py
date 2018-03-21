def to_bin(x):
    """
    Inputs:\n
    x - intiger number\n
    ------------------\n
    Output:\n
    string - the representation of x in binaries
    """
    a=""
    for i in range(11):
        a += str(x%2) + "\n"
        x /= 2
    return a[::-1]

def more_byte(x):
    """
    Inputs:\n
    x - intiger number\n
    ------------------\n
    Output:\n
    string - more frequent bit in binary representation of x
    """
    x=bin(x)[2:]
    a=0
    for i in range(len(x)):
        if x[i] == "1":
            a += 1
    if a >= len(x)/2:
        return "1"
    else:
        return "0"

def xor_byte(x):
    """
    Inputs:\n
    x - intiger number\n
    ------------------\n
    Output:\n
    string - score of operation xor made on bits of binary representation fo x
    """
    x = bin(x)[2:]
    a = x[0]
    for i in range(1, len(x)):
        if a == x[i]:
            a = "0"
        else:
            a = "1"
    return a

def gen_afi_body(x0, a, b, M, n):
    """
    Inputs:\n
    x0 - intiger number, seed for generator\n
    a, b, M - integers, constant for generator\n
    n - integer, len of output file\n
    ------------------\n
    Output:\n
    string - n bits generated from generator LCG
    """
    begin = x0
    out = ""
    for i in range(n):
        xn = (a * x0 + b) % M
        out += xor_byte(xn)
        x0 = xn
        if x0 == begin:
            print i
    return out

def gen_LCG(x0, n, file_name):
    """
    Inputs:\n
    x0 - intiger number, seed for generator\n
    n - integer, len of output file\n
    file_name - string, name of creating file with result\n
    ------------------\n
    Output:\n
    integer - lenght of creating file
    """
    out = gen_afi_body(x0,pow(2,10)+1,7949,pow(2,20),n)
    file_out = open(file_name,'w')
    file_out.write(out[1:])
    file_out.close()

if __name__ == '__main__':
    for i in range(20):
        gen_LCG(i,20001,"afiniczny/af_xor"+str(i+1)+".txt")

