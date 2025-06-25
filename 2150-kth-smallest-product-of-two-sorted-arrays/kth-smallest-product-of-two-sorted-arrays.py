import bisect

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        def countLessEqual(x):
            count = 0
            for a in nums1:
                if a > 0:
                    
                    r = bisect.bisect_right(nums2, x // a)
                    count += r
                elif a < 0:
    
                    y = x // a
                    if x % a:
                        y += 1
                    l = bisect.bisect_left(nums2, y)
                    count += len(nums2) - l
                else:  
                    if x >= 0:
                        count += len(nums2)
            return count

       

        lo, hi = -10**10, 10**10
        while lo < hi:
            mid = (lo + hi) // 2
            if countLessEqual(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo
