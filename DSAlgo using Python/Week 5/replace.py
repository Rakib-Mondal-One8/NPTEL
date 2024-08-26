import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
s = "brown fox gray dogs brown fox"
s = s.replace("brown","Red",1)
print(s)