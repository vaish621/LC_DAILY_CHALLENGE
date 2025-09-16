class Solution:
    def numTrees(self, n: int) -> int:

        numTree=[1]*(n+1)

        for nodes in range(2,n+1):
            tot=0
            for root in range(1,nodes+1):
                le=root-1
                re=nodes-root
                tot+=numTree[le]*numTree[re]
            numTree[nodes]=tot
        
        return numTree[n]

        
        