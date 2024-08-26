import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
def frequency(l):
    map = {}
    for e in l:
        if e in map.keys():
            map[e]+=1
        else : map[e] = 0
    e1 = []
    e2 = []
    v1 = sys.maxsize
    v2 = -1*sys.maxsize
    for e in l:
        if(map[e]<v1):
           v1 = map[e]
        if(map[e]>v2):
            v2 = map[e]
    p1 = 0
    p2 = 0
    for e in sorted(map.keys()):
        if((map[e]==v1)):
            e1.append(e)
        if(map[e]==v2):
            e2.append(e)
    return (e1,e2)
print(frequency([4,4,4,1,1,2,2,2,3,3]))
