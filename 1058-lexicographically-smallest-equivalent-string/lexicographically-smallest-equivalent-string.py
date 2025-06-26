class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """

        parent={}

        def find(x):

            if x!=parent.setdefault(x,x):
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                if px<py:
                    parent[py]=px
                else:
                    parent[px]=py
        
        ans=[]

        for x,y in zip(s1,s2):
            union(x,y)
        
        for f in baseStr:
            ans.append(find(f))
        
        return "".join(ans)

                

        