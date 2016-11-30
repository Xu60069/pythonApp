import random

MAX_WHITE=69
MAX_RED=26

class PowerBallDraw:
    def __init__(self):
        self.whites = [0,0,0,0,0];
        self.power = 0;

    def draw(self):
        count = 0;
        self.whites = [0,0,0,0,0];
        while (count<5):
            newOne = random.randint(1,MAX_WHITE);
            if (newOne in self.whites):
                continue;
            self.whites[count] = newOne;
            count += 1;
        self.whites.sort();
        self.power = random.randint(1,MAX_RED);
                    
num = random.randint(1,MAX_WHITE);
print(num);
white_balls=[1,2,3,4,5];
Winner=[32,16,19,57,34];
Winner.sort();
Winner_pow = 13;
for num in range(0,4):
    white_balls[num] = random.randint(1,MAX_WHITE);
print(white_balls);
white_balls.sort();
print(white_balls);
if ( white_balls == Winner ):
    print("Won");
else:
    print("lost");

ticketsfile = open("powerball.txt","w");
powerball = PowerBallDraw();
draws=1;
while (1):
    powerball.draw();
    draws += 1;
    for item in powerball.whites:
        ticketsfile.write(str(item)+',');
    ticketsfile.write(str(powerball.power)+'\n');
    if ( draws%50000==0 ):
        print(powerball.whites);
        print("Draw " + str(draws));
    if ( (powerball.whites == Winner) and (powerball.power==Winner_pow)):
        print("Won Jackpot tickets No " + str(draws));
        ticketsfile.write("Won Jackpot tickets No " + str(draws)+'\n');
        break;

