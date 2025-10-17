class Solution:
    def takeCharacters(self, nums: str, k: int) -> int:
        c=collections.Counter(nums)

        if k==0:
            return 0

        if 'a' not in c or 'b' not in c or 'c' not in c:
            return -1
        
        if c['a']<k or c['b']<k or c['c']<k:
            return -1

        st=0
        en=0

        ans=0

        while en<len(nums):
            c[nums[en]]-=1
            if c[nums[en]]<k:

                while st<=en and c[nums[en]]<k:
                    c[nums[st]]+=1
                    st+=1
            
            ans=max(ans,en-st+1)
            en+=1
        
        return len(nums)-ans
        