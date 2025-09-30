class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize!=0:
            return False

        c=collections.Counter(hand)

        hand.sort()

        count=0

        for j in hand:
            ch=j
            i=0
            
            while i<groupSize:
                if ch in c:
                    if c[ch]>0:
                        c[ch]-=1
                        ch+=1
                        i+=1
                    else:
                        break
                else:
                    break
            
            #print(i)
            if i==groupSize:
                count+=i
        
        if count==len(hand):
            return True
        else:
            return False


        