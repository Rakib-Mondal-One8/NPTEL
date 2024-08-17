def merge(a,b):
    (c,m,n) = ([],len(a),len(b))
    i = 0
    j = 0
    while(i+j<m+n):
        if(i==m):
            c.append(b[j])
            j = j+1
        elif(j==n):
            c.append(a[i])
            i=i+1
        elif(a[i]<b[j]):
            c.append(a[i])
            i = i+1
        else:
            c.append(b[j])
            j = j+1
    return c
def mergesort(a,l,r):
    if(r-l <=1):
        print(l)
        print(r)
        print(a[l:r])
        return a[l:r]
    if(r-l>1):
        mid = (l+r)//2
        L = mergesort(a,l,mid)
        R = mergesort(a,mid,r)
        return merge(L,R)

list = [3,2,1,60,10]
list = mergesort(list,0,len(list))
print(list)
