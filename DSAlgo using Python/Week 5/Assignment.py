import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#---------------------------------------------------------------------------------------------------------------------#
Books = {}
Borrowers = {}
Checkouts = {}
ans = []
def check():
    while(True):
        s = input()
        if(s=="EndOfInput"):break
        s = s.replace("~"," ",2)
        s = s.replace("-"," ",1)
        x = s.split()
        res = ""
        res+=(x[3]+"~")
        res+=(Borrowers[x[0]]+"~")
        res+=(x[1]+"-"+x[2]+"~")
        res+=(Books[x[1]][x[2]])
        ans.append(res)
def borrow():
    while(True):
        s = input()
        if(s=="Checkouts"):break
        s = s.replace('~'," ")
        x = s.split()
        res = ""
        for i in range(1,len(x)):
            res+=(x[i]+" ")
        res = res.strip()
        Borrowers[x[0]] = res
    check()
def book():
    while(True):
        s = input()
        if(s == "Borrowers"):break;
        s = s.replace("-", " ",1)
        s = s.replace("~"," ")
        x = s.split()
        def ini():
                res = ""
                for j in range(2,len(x)):
                    res+=(x[j]+" ")
                res = res.strip()
                Books[x[0]][x[1]] = res
        if(x[0] in Books):
            if(x[1] in Books[x[0]]):
                ini()
            else:
                Books[x[0]][x[1]] = {}
                ini()
        else:
            Books[x[0]]={} 
            if(x[1] in Books[x[0]]):
                ini()
            else:
                Books[x[0]][x[1]] = {}
                ini()
    borrow()
t = input()          
book()
for e in sorted(ans):
    print(e)