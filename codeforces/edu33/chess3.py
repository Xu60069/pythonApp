#chess for 3, edu 33 A
#Alex (#1) play with Bob (#2) in first game, Carl(#3) is spectating
#loser of previous will be spectator
#find if the log of winners is valid

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

def solve():
    games=ni()
    winner=[None]*games
    for i in range (games):
        winner[i]=ni()
    last=winner[0]
    if last==3:     #special case, first game winner must be 1 or 2
        return False
    loser=3-last
    spect=3
    for i in range(1, games):
        if winner[i]==last:     #same winner, swap spect and loser
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
