class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        
        if len(target)>len(s):
            return 0
        d={}
        d1={}

        for i in target:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1

        for i in s:
            if i in target:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        
        ma=float('inf')
        co=0
        for k,v in d.items():
            if d[k]>=d1[k]:
                ma=min(ma,d[k]//d1[k])
                co+=1
        
        if co==len(d1):
            if ma==float('inf'):
                return 0
            return ma
        else:
            return 0

        