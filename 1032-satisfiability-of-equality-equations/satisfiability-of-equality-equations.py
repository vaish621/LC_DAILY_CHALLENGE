class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

    

        parent=[i for i in range(26)]
        rank=[0]*26

        def find(x):

            if x==parent[x]:
                return x
            
            parent[x]=find(parent[x])

            return parent[x]
        
        def union(x,y):
            px,py=find(x),find(y)

            if px==py:
                return
            
            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[py]>rank[px]:
                parent[px]=py
            else:
                parent[px]=py
                rank[py]+=1
        
        for i in equations:
            ch=i[0]
            ch1=i[-1]
            eq=ord(ch)-ord('a')
            eq2=ord(ch1)-ord('a')

            if i[1:3]=="==":
                union(eq,eq2)
        
        for i in equations:
            ch=i[0]
            ch1=i[-1]
            eq=ord(ch)-ord('a')
            eq2=ord(ch1)-ord('a')

            if i[1:3]=="!=":
                f1=find(eq)
                f2=find(eq2)

                if f1==f2:
                    return False

        
        return True


        