import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
date = "26"
month = "Aug"
year = "2024"
today = "-".join([date,month,year])
print(today)
print("/".join(["24","August","2024"]))