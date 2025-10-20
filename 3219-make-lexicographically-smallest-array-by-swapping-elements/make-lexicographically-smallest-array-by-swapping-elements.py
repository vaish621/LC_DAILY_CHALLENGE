class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        org=[]

        for i in nums:
            org.append(i)

        nums.sort()
        
        beg=0
        d={}
        d[0]=[]
        d[0].append(nums[0])

        numtoind=defaultdict(int)
        numtoind[nums[0]]=0

        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]<=limit:
                if beg not in d:
                    d[beg]=[]
                d[beg].append(nums[i])
                numtoind[nums[i]]=beg
            else:
                beg+=1
                if beg not in d:
                    d[beg]=[]
                d[beg].append(nums[i])
                numtoind[nums[i]]=beg
        
        ans=[]
        
        for i in org:
            find=numtoind[i]

            if len(d[find])>0:
                ans.append(d[find][0])
                d[find].pop(0)
        
        return ans

        
        
        
        

        