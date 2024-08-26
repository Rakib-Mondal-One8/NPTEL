import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
s = "6,7,8,9"
s = s.split(",")
new_s = "6?#7?#9?#10"
new_s = new_s.split("#")
print(new_s)