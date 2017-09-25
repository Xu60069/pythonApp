class Game123:
    def __init__(self):
        self.alice = [0]*9
        self.bob=[0]*9
        self.moves=[-1]*10
        self.count=0

    def gameChoice(self, m, r, bBob):
        choice=self.alice
        if bBob:
            choice=self.bob
        for i in range(len(m)):
            choice[3*r+i]=m[i]

    def findMove(self, a, b):
        m=(a-1)*3+b-1
        for i in range(self.count):
            if self.moves==m:
                return i
        self.moves[self.count]=m
        self.count += 1
        return -1
        
        
    def startGame(self, a, b):
        repeat
        while self.findMove(a,b)<0:
            m=(a-1)*3+b-1
            a=self.alice[m]
            b=self.bob[m]
        
