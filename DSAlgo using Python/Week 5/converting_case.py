import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
s = "rakib Mondal"
# s = s.capitalize()
s = s.lower()
s = s.upper()
print(s)