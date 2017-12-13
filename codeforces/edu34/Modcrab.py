#edu round 34, B
#game rules
# each phase or round, Vovo attack, monster attack, or vova heal, monster
# Initially vova attack power a1, health h1, unlimited potion with c1 health points 
#   Monster attack power a2, health h2
# Vova can attack monster and redcue its health by a1 points,
#  or heal and gain c1 points
# if not lost (health<=0), Modcrab then attach Vova, reduce her points by a2
def ceiling(num, denom):
    return (num+denom-1)//denom

def strategy(h1, a1, c1, h2, a2):
    strikes=ceiling(h2, a1)  # need at least this many phases to kill monster
    health=a2*(strikes-1)+1  # need at least this much health to not lose
    potion=0
    if h1<health:
        potion=ceiling(health-h1, c1-a2) # each potion only gain c1-a2 health
    print(potion+strikes)
    while potion>0:
        print("HEAL")
        potion -= 1
    while strikes>0:
        print("STRIKE")
        strikes -= 1

def test():
    strategy(10, 6, 100, 17, 5)
    strategy(11, 6, 100, 12, 5)
    strategy(9, 6, 6, 17, 5)

def nia():
    s=input()
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal

vivo=nia()
monster=nia()
strategy(vivo[0], vivo[1],vivo[2], monster[0], monster[1])
