# 3 states in order: C E S
def solve(s):
    last='\0'
    for c in s:
        if c=='E':
            if last=='S':
                print("no")
                return
        elif c=='C':
            if last=='S' or last=='E':
                print("no")
                return
        last=c
    print("yes")

def test():
    solve("CES")
    solve("CS")  
    solve("CCC")    
    solve("SC")    
    solve("ECCC")

n=int(input())
for i in range(n):
    solve(input())
