import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
l = [1,3,4,5,6,7,8]
def iseven(x):return(x%2==0)
def sq(x):return x*x
print(list(map(sq,filter(iseven,l))))
# filter pass the value to map if iseven property is true.
# Otherwise it skips that value