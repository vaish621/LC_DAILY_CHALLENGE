class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort()

        h=[]

        st=events[0][0]

        j=0
        ans=0

        while(j<len(events) or len(h)>0):
            while(j<len(events) and events[j][0]<=st):
                heapq.heappush(h,events[j][1])
                j+=1
            
            if h:
                heapq.heappop(h)
                ans+=1
            
            st+=1
        
            while(h and h[0]<st):
                heapq.heappop(h)
            
           
        
        return ans


        
        