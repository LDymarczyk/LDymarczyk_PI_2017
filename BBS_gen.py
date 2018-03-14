from pseudolosowy_afiniczny import xor_byte, more_byte

def BBSgen_body(x0, p, q):
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


def BBSgen(x, n, k, file_name):
    """
    Inputs:\n
    x - intiger number, seed for generator\n
    n - intiger, length of generating string of bytes\n
    k - string, number added at the end of file name\n
    file_name - string, name of creating file with result\n
    ------------------\n
    Output:\n
    None, but saving generated n bytes to file
    """
    begin = x
    outs, outx, outm = "", "", ""
    for i in range(n):
        res = BBSgen_body(x, 1287467, 4243067)
        x = res[0]
        outs += res[1]
        outx += res[2]
        outm += res[3]
        if x==begin:
            print i
    file_out = open(file_name+"sb"+k+".txt",'w')
    file_out.write(outs)
    file_out.close()
    file_out = open(file_name+"xb"+k+".txt",'w')
    file_out.write(outx)
    file_out.close()
    file_out = open(file_name+"mb"+k+".txt",'w')
    file_out.write(outm)
    file_out.close()
        

if __name__ == '__main__':
    for i in range(20):
        BBSgen(201, 20000, str(i+1), "bbs/BBS")
    BBSgen(201, 1000000, "", "bbs/BBS_for_test_walk")
