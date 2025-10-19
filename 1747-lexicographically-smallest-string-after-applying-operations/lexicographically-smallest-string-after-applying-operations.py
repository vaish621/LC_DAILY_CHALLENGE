class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        q=deque()
        visit=set()

        q.append(s)
        visit.add(s)
        ans=s

        while q:
            t=q.popleft()
            if t<ans:
                ans=t
            
            #add a
            ne=""
            for i in range(len(t)):
                if i%2!=0:
                    ne+=str((int(t[i])+a)%10)
                else:
                    ne+=t[i]
            
            if ne not in visit:
                visit.add(ne)
                q.append(ne)
            
            #rotate b steps

            rot=t[::-1][:b][::-1]+t[::-1][b:][::-1]
            

            if rot not in visit:
                visit.add(rot)
                q.append(rot)
        
        return ans
        