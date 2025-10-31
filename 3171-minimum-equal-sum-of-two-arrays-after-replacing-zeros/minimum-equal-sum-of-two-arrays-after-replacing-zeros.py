class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1=sum(nums1)
        s2=sum(nums2)
        co1=nums1.count(0)
        co2=nums2.count(0)

        if co1==0 and co2==0:
            if s1!=s2:
                return -1
            return s1
        elif co1==0:
            return s1 if s2+co2<=s1 else -1
        elif co2==0:
            return s2 if s1+co1<=s2 else -1
        else:
            return max(s1+co1,s2+co2)