class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        def topx(mp):
            h=[]
            for k,v in mp.items():
                heapq.heappush(h,[v,k])
                while h and len(h)>x:
                    heapq.heappop(h)
            
            su=0

            while h:
                val,key=heapq.heappop(h)
                su+=key*val
            
            return su
        

        d=defaultdict(int)
        st=0
        en=0
        ans=[]

        while en<len(nums):
            d[nums[en]]+=1
            
            if en-st+1==k:
                ans.append(topx(d))
                d[nums[st]]-=1
                if d[nums[st]]==0:
                    del d[nums[st]]
                st+=1
            
            en+=1
        
        return ans

        