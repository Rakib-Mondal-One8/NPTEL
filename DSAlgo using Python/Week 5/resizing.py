import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
s = "hello"
# s = s.center(50,'-')
# s = s.ljust(50,'-') # Prints spaces in the right side
s = s.rjust(50,'-') # Prints spaces in the left side
print(s)