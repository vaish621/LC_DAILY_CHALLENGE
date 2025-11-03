class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        segtree=[0]*(4*n)

        def build(i,l,r):
            if l==r:
                segtree[i]=baskets[l]
                return
            
            mid=(l+r)//2
            
            build(2*i+1,l,mid)
            build(2*i+2,mid+1,r)

            segtree[i]=max(segtree[2*i+1],segtree[2*i+2])
        
        def placing(i,l,r,fruit):
            if segtree[i]<fruit:
                return False
            
            if l==r:
                segtree[i]=-1
                return True
            
            mid=(l+r)//2
            
            ans=False
            if segtree[2*i+1]>=fruit:
                ans=placing(2*i+1,l,mid,fruit)
            elif segtree[2*i+2]>=fruit:
                ans=placing(2*i+2,mid+1,r,fruit)
            
            segtree[i]=max(segtree[2*i+1],segtree[2*i+2])

            return ans
        
        build(0,0,len(baskets)-1)

        result=0

        for i in fruits:
            if not placing(0,0,n-1,i):
                result+=1
        
        return result
        