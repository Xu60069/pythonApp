#chess for 3, edu 33 A

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

def nia():
    s=input()
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal

def solve():
    games=ni()
    winner=[0]*games
    for i in range (games):
        winner[i]=nia()
    last=winner[0]
    loser=0
    spect=0
    for i in range(1, games):
        if winner[i]==last and loser==0:
            continue
        if loser==0:  #first time 2 diff winner
            loser=last
            last=winner[i]
            for j in range (1,4):
                if j!=loser and j!=last:
                    spect=j
        elif winner[i]==last:
            temp=loser
            loser=spect
            spect=temp
        else:
            if winner[i]==loser:  #new winner cannot be last loser
                return False
            else:
                spect=loser
                loser=last
                last=winner[i]
    return True

if solve():
    print("YES")
else:
    print("NO")
