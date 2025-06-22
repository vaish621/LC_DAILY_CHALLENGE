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
            print(x,px,y,py)
            if px!=py:
                if px<py:
                    parent[py]=px
                else:
                    parent[px]=py

        for a,b in zip(s1,s2):
            union(a,b)

        return "".join(find(c) for c in baseStr)

        