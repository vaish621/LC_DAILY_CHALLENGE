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
        
        if co1==len(nums1) and co2==len(nums2):
            return max(len(nums1),len(nums2))

        def can_do(mid):
            if s1>mid or s2>mid:
                return False
            
            if co1!=0 and co2!=0:
                if mid-s1<co1 or mid-s2<co2:
                    return False
                return True
            else:
                if co1==0:
                    if s1!=mid:
                        return False
                    if mid-s2<co2:
                        return False
                    return True
                else:
                    if s2!=mid:
                        return False
                    if mid-s1<co1:
                        return False
                    return True
           
        l=1
        r=max(s1,s2)*2
        ans=-1

        while l<=r:
            mid=(l+r)//2
            if can_do(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        
        return ans

        