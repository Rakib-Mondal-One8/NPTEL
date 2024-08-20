import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#---------------------------------------------------------------------------------------------------------------------#
def onehop(l):
    path = {}
    for (i,j) in l:
        path[i]=[]
    for(i,j)in l:
        path[i].append(j)
    res = []
    for val in path.keys():
        for d in path[val]:
            if(d in path):
                for e in path[d]:
                    if (val,e) not in res and (val!=e):res.append((val,e))
    res.sort()
    return res

print(onehop([(1,2),(3,2)]))