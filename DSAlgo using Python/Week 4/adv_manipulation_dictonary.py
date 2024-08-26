import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
score = {"test1":{"kohli":100,'rakib':200,'dhawan':87},
         "test2":{'rakib':100,'kohli':250,'pujara':50},
        "test3":{'rakib':10,'kohli':50,'dhawan':20}
         }
tot = {}
for p in ['rakib','kohli','dhawan']:
    tot[p] = 0;
    for match in score.keys():
        if p in score[match].keys():
            tot[p]+=score[match][p]

print(tot)
