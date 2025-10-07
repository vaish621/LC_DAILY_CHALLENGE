import bisect

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        ans=0

        i=0

        while i<len(players) and trainers:
            t=bisect.bisect_left(trainers,players[i])
            #print(t,trainers)

            if t==0:
                if trainers[t]>=players[i]:
                    trainers.pop(t)
                    ans+=1
            else:
                if t<len(trainers):
                    trainers.pop(t)
                    ans+=1
            i+=1
        
        return ans
        

        