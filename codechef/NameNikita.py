#format name as F. M. Lastname, each line could contain 1 or 2 or 3 names
def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

def ns():
    s=input()
    while len(s)==0:
        s=input()
    return s

def initial(name):
    if (len(name)>0):
        name=name[0]+"."
        return name.upper()
    return name

def parseLine(line):
    s=line.split()
    size=len(s);
    for i in range (size):
        if i==size-1:
            print(s[i].capitalize())
        else:
            print(initial(s[i])+" ", end="")         
    
def solve():
    n=ni()
    while (n > 0):
        n -= 1
        parseLine(ns())

def test():
    parseLine("gandhI")
    parseLine("mahatma gandhI")
    parseLine("Mohndas KaramChand gandhi")

solve()
