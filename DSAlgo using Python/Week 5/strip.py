import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
s = " Rakib Mondal "
s = s.rstrip()
s = s.lstrip()
s = s.strip() # For removing whitespace from both leading and trailing.
print(s)