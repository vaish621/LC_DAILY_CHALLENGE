
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * n  
        for i in range(n):
            diff[max(0, i - r)] += stations[i]
            if i + r + 1 < n:          
                diff[i + r + 1] -= stations[i]

        def can_achieve(mid):
            temp = diff.copy()
            cur_sum = 0
            rem = k

            for i in range(n):
                cur_sum += temp[i]
                if cur_sum < mid:
                    need = mid - cur_sum
                    if need > rem:
                        return False
                    rem -= need
                    cur_sum += need
                    if i + 2*r + 1 < n:   
                        temp[i + 2*r + 1] -= need
            return True

        l = min(stations)
        right = sum(stations) + k
        ans = 0

        while l <= right:
            mid = (l + right) // 2
            if can_achieve(mid):
                ans = mid
                l = mid + 1
            else:
                right= mid - 1

        return ans
