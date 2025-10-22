class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        freq=defaultdict(int)
        modes=set()
        nums.sort()
        beg=0
        ans=0

        def add_mode(val):
            modes.add(val)

            if val-k>=nums[0]:
                modes.add(val-k)
            
            if val+k>=nums[-1]:
                modes.add(val+k)

        for i in range(len(nums)):
            if nums[i]!=nums[beg]:
                freq[nums[beg]]=i-beg
                ans=max(ans,freq[nums[beg]])
                add_mode(nums[beg])
                beg=i
        
        freq[nums[beg]]=len(nums)-beg
        add_mode(nums[beg])
        ans=max(ans,freq[nums[beg]])

        for i in sorted(modes):
            l=bisect.bisect_left(nums,i-k)
            r=bisect.bisect_right(nums,i+k)-1

            if i in freq:
                t=min(r-l+1,freq[i]+numOperations)
            else:
                t=min(r-l+1,numOperations)
            
            ans=max(ans,t)
        
        return ans
        