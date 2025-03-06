class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        ind=p.index('*')
        h=p[0:ind]
        t=p[ind+1:len(p)]
        
        n=s.find(h)
        m=s.rfind(t)

    
        if m!=-1 and n!=-1 and n+len(h)<=m:
            return True
        return False
