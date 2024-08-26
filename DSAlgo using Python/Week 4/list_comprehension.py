import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
l = [1,2,3,4]
def f(x):return x**2
print(list(map(f,l))) 

print([f(i) for i in range(10) if (i%2==0)])