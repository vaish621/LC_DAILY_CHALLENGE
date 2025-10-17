class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atmost(k1):
            d=defaultdict(int)
            st=0
            en=0

            ans=0
            while en<len(nums):
                d[nums[en]]+=1

                while st<=en and len(d)>k1:
                    d[nums[st]]-=1
                    if d[nums[st]]==0:
                        del d[nums[st]]
                    st+=1
                
                ans+=en-st+1
                en+=1
            
            return ans
        
        return atmost(k)-atmost(k-1)

        



        