class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:



        dist1=[float("inf")]*len(edges)
        dist2=[float("inf")]*len(edges)

        


        def dfs(i,fl,cu,visit):
            if i in visit or i==-1:
                return
            visit.add(i)
            if fl==0:
                dist1[i]=cu
            else:
                dist2[i]=cu
            
            dfs(edges[i],fl,cu+1,visit)
        

        visit=set()
        dfs(node1,0,0,visit)
        visit=set()
        dfs(node2,1,0,visit)

        mi=float("inf")
        index=-1

        #print(dist1,dist2)
        
        for i in range(len(dist1)):
            ma=max(dist1[i],dist2[i])
            if ma<mi:
                mi=ma
                index=i
        
        return index


    
            
        