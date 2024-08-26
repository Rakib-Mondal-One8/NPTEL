import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
def update(x):
    x[2] = 100
x = [2,3,4,50]
y = x
y[3] = 5
update(x)
print(x[2])
print(x[3]) # if we assign a mutable to another name..
# From another name it is possible to change the original mutable object