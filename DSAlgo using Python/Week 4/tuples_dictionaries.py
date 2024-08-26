import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
t = ()
d = {}
# print(type(t))
# print(type(d))
d = {"rajesh ": 21,"Rakib":18,"test":{'rakib':100,'kohli':200}} # test is dictonary inside a dictionary
"""
print(d['Rakib'])
d["Rakib"] = 19
print(d["Rakib"])
print(d['test']['rakib']) 

"""
for k in d.keys():
    print(k)
for k in sorted(d.keys()):
    print(k)
print(sorted(d))
print(d)