class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        d={}

        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]]=[]
            d[groupSizes[i]].append(i)
        
        so=dict(sorted(d.items()))
        ans=[]

        for k,v in so.items():
            ch=0
            while ch<len(v):
                ans.append(v[ch:ch+k])
                ch+=k
        
        

        return ans
        