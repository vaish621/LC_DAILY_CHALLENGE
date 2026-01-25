class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

        for i in range(n):
            if leftChild[i]!=-1:
                if leftChild[i] in rightChild:
                    return False
            
            if rightChild[i]!=-1:
                if rightChild[i]!=-1:
                    if rightChild[i] in leftChild:
                        return False
        
        def detectcycle(node,vis):
            if node in vis:
                return True
            
            vis.add(node)

            if leftChild[node]!=-1:
                if detectcycle(leftChild[node],vis):
                    return True
            
            if rightChild[node]!=-1:
                if detectcycle(rightChild[node],vis):
                    return True
            
            return False



        parent=[i for i in range(n)]

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            
            return parent[x]
        
        rank=[0 for i in range(n)]
        def union(x,y):
            px,py=find(x),find(y)

            if px==py:
                return
            
            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[py]>rank[px]:
                parent[px]=py
            else:
                parent[py]=px
                rank[px]+=1
        
        for i in range(n):
            if leftChild[i]!=-1:
                union(i,leftChild[i])
            
            if rightChild[i]!=-1:
                union(i,rightChild[i])
        
        s=set(parent)
        print(s)

        if len(s)>2:
            return False

        if len(s)==2:
            nodesfound=0
            for i in s:
                    vis=set()

                    if detectcycle(i,vis):
                        print("m")
                        return False
                    
                    nodesfound=max(nodesfound,len(vis))
                    
            if nodesfound!=n:
                return False
            return True
        else:
            t=list(s)
            vis=set()
            if detectcycle(t[0],vis):
                return False
            
            return True
            
            
                
                
            
            

        



        