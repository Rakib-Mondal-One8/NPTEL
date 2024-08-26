import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
s = "Rakib Loves to play badminton"
print(s.find("Rakib",6,len(s)))