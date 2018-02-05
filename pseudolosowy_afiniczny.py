def to_bin(x):
    """
    Inputs:
    x - intiger number
    ------------------
    Output:
    string - the representation of x in binaries
    """
    a=""
    for i in range(11):
        a += str(x%2) + "\n"
        x /= 2
    return a[::-1]

def more_bite(x):
    """
    Inputs:
    x - intiger number
    ------------------
    Output:
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

def xor_bite(x):
    """
    Inputs:
    x - intiger number
    ------------------
    Output:
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
    Inputs:
    x0 - intiger number, seed for generator
    a, b, M - integers, constant for generator
    n - integer, len of output file
    ------------------
    Output:
    string - n bits generated from generator LCG
    """
    begin = x0
    out = ""
    for i in range(n):
        xn = (a * x0 + b) % M
        out += more_bite(xn)
        x0 = xn
        if x0 == begin:
            print i
    return out

def gen_LCG(x0, n, file_name):
    """
    Inputs:
    x0 - intiger number, seed for generator
    n - integer, len of output file
    file_name - string, name of creating file with result
    ------------------
    Output:
    integer - lenght of creating file
    """
    out = gen_afi_body(x0,872323,7949,2097152,n)
    file_out = open(file_name,'w')
    file_out.write(out[1:])
    file_out.close()

if __name__ == '__main__':
    for i in range(20):
        gen_LCG(i,20000,"afiniczny/af_more"+str(i+1)+".txt")
    gen_LCG(1,1000000,"afiniczny/af_more_for_test_walk.txt")
