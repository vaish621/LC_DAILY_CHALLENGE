import heapq
class Solution(object):
    def specialNodes(self, n, edges, x, y, z):
        """
        :type n: int
        :type edges: List[List[int]]
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(start):
            

            dj=[float("inf")]*n
            dj[start]=0

            h=[]
            heapq.heappush(h,[0,start])
                
            vis=set()
                
            while h:
                    #print(h)
                    dis,node=heapq.heappop(h)
                    vis.add(node)
                    if dis<dj[node]:
                        dj[node]=dis
                    
                    for j in adj[node]:
                        if j!=node and j not in vis:
                            heapq.heappush(h,[dis+1,j])
                
            return dj
            
        dx=bfs(x)
        dy=bfs(y)
        dz=bfs(z)

        #print(dx,dy,dz)
        ans=0

        for i in range(n):
            t=[dx[i],dy[i],dz[i]]
            t.sort()
            if t[0]*t[0]+t[1]*t[1]==t[2]*t[2]:
                ans+=1
        
        return ans
         

            