import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
s = "first num {}, Second {}".format(18,19)
print(s)
a = "One : {f}, Two : {s}".format(s=20,f=21)
print(a)

# Real Formatting 
a = "Value : {0:3d}".format(5)
print(a)
a = "Value : {0:6.3f}".format(18.123)
print(a)