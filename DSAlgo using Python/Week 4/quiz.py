import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#*----------------------------------------------------------------------------------------*#
# What does mystery([22,14,19,65,82,55]) return?

"""
def mystery(l):
    print(l)
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])
print(mystery([22,14,19,65,82,55]))
"""
# What is the value of pairs after the following assignment?
"""
pairs = [ (x,y) for x in range(4,1,-1) for y in range(5,1,-1) if (x+y)%3 == 0 ]
print(pairs)
"""
# Which of the following statements does not generate an error?

"""
wickets = {"Tests":{"Bumrah":[3,5,2,3],"Shami":[4,4,1,0],"Ashwin":[2,1,7,4]},
           "ODI":{"Bumrah":[2,0],"Shami":[1,2]}}

wickets["ODI"]["Ashwin"] = [4,4]
print(wickets["ODI"]["Ashwin"])
"""

# Which of the following generates an error?

hundreds = {}
hundreds[["Tendulkar","international"]] = 100
print(hundreds['Tendulkar','international'])