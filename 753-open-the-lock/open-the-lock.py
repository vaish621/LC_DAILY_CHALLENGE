class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        locks=[ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        q=deque()

        q.append("0000")
        

        visit=set()
        visit.add("0000")
        time=0

        while q:

            for i in range(len(q)):
                t=q.popleft()
                if t==target:
                    return time
                for j in range(len(t)):
                    if t[j]=="9":
                        ne=t[0:j]+"0"+t[j+1:]
                    else:
                        ne=t[0:j]+str(int(t[j])+1)+t[j+1:]
                    if t[j]=="0":
                        ne2=t[0:j]+"9"+t[j+1:]
                    else:
                        ne2=t[0:j]+str(int(t[j])-1)+t[j+1:]
                    
                    if ne not in visit and ne not in deadends:
                        q.append(ne)
                        visit.add(ne)
                    if ne2 not in visit and ne2 not in deadends:
                        q.append(ne2)
                        visit.add(ne2)

                                
            time+=1
        
        return -1


        