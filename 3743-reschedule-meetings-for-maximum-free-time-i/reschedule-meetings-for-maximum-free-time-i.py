class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        f=[]

        f.append(startTime[0])

        for i in range(1,len(startTime)):
            f.append(startTime[i]-endTime[i-1])
        
        f.append(eventTime-endTime[-1])

        nk=k+1

        st=0
        en=0

        ans=0
        su=0

        while en<len(f):

            su+=f[en]
            if en-st+1>nk:
                su-=f[st]
                st+=1
            
            ans=max(ans,su)
            en+=1
        
        


        return (ans)
        
        
        