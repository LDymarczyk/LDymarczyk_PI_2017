from math import atan2, sqrt, sin, pi

def biegunowy_body(point1, point2):
    """
    Inputs:\n
    points - list with 2 arguments [x, y]\n
    ------------------\n
    Output:\n
    polar variable [a, b]
    """
    x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]
    a=sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    b=180*atan2(y2-y1,x2-x1)/pi
    if b<=0:
        b=360-b
    return (a, b)

def biegunowy(points):
    """
    Inputs:\n
    points - list of points [xi, yi]\n
    ------------------\n
    Output:\n
    list of polar variables [ai, bi]
    """
    ret = []
    for i in range(len(points) - 1):
        p = biegunowy_body(points[i], points[i + 1])
        ret.append(p)
    return ret

def chaos_map_body(point):
    """
    Inputs:\n
    points - list with 2 arguments [x, y]\n
    ------------------\n
    Output:\n
    list with 2 arguments [a, b] after chaotic mapping
    """
    x, y = point[0], point[1]
    N = 1024
    K = 5743
    a = (x + y) % N
    b = (y + K * sin(N) / 2 * pi) % N
    return (a, b)

def chaos_map(points):
    """
    Inputs:\n
    points - list of lists with 2 arguments [xi, yi]\n
    ------------------
    Output:\n
    list of lists with 2 arguments [ai, bi] after chaotic mapping
    """
    ret=[]
##    print type(points)
    for i in range(len(points)):
        p = chaos_map_body(points[i])
        ret.append(p)
    return ret

#print chaos_map([[1,2],[2,3]])
