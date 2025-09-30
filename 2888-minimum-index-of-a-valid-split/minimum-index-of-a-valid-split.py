class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        c=collections.Counter(nums)
        n=len(nums)

        i=0

        m1=defaultdict(int)

        while i<len(nums):
            m1[nums[i]]+=1
            c[nums[i]]-=1

            if m1[nums[i]]>(i+1)//2 and c[nums[i]]>(n-i-1)//2:
                return i
            
            i+=1
        

        return -1
            

        