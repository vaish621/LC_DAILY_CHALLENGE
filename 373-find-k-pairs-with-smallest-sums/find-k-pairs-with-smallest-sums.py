import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []

        hea = []
        heapq.heappush(hea, (nums1[0] + nums2[0], 0, 0))
        vis = set()
        vis.add((0, 0))
        ans = []

        while k > 0 and hea:
            s, i, j = heapq.heappop(hea)
            ans.append([nums1[i], nums2[j]])
            k -= 1

            if i + 1 < len(nums1) and (i + 1, j) not in vis:
                heapq.heappush(hea, (nums1[i + 1] + nums2[j], i + 1, j))
                vis.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in vis:
                heapq.heappush(hea, (nums1[i] + nums2[j + 1], i, j + 1))
                vis.add((i, j + 1))

        return ans
