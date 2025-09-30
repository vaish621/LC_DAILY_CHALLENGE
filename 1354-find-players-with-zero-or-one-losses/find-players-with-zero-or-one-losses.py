class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        win=defaultdict(int)
        los=defaultdict(int)

        for u,v in matches:
            win[u]+=1
            los[v]+=1
        
        win=dict(sorted(win.items()))
        los=dict(sorted(los.items()))

        ans=[]

        res=[]
        
       

        for k,v in win.items():
            if k not in los:
                res.append(k)

        ans.append(res)
        res=[]

        for k,v in los.items():
            if v==1:
                res.append(k)
        
        ans.append(res)
        
        return ans