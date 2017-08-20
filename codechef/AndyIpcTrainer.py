import heapq
for __ in range(int(input())):
    N,D = map(int,input().split()) # N trainers, D camp days
    trainerinfo = []
    heap = []
    ans = 0
    for _ in range(N):
        Di,Ti,Si = map(int,input().split())
        trainerinfo.append((-1*Si,Di,Ti))       # use negative sadness so heap is sorted by max sadness
        ans += Si*Ti  # add up total sadness
    trainerinfo.sort(key = lambda tup: tup[1])  # sort trainer by day arrived
    #print(trainerinfo)
    c, t = 0, 1  # start with day 1
    while t <= D and c < N+1: # N+1 allow to process on last day
        if c<N and trainerinfo[c][1] == t: # add trainer to heap when arrival day match current day
            heapq.heappush(heap,trainerinfo[c])
            #print(heap)
            c+=1
        else: #pick a trainer for lecture on t day
            if len(heap) > 0:
                info = heapq.heappop(heap)  # find trainer with largest sadness
                #print("pick on day {0} :{1}".format((t-1),info))
                ans += info[0]
                update = (info[0],info[1],info[2]-1)
                if update[2]>0:  # add back trainer if he still needs more lectures
                    heapq.heappush(heap,update)
            t+=1  # increment to next dat
    print (ans)
