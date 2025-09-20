import bisect


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        combine = sorted(zip(difficulty, profit))

        prefix = [0] * len(combine)
        prefix[0] = combine[0][1]

        for i in range(1, len(prefix)):
            prefix[i] = max(prefix[i-1], combine[i][1])

        print(prefix)

        diff = [i for i, j in combine]
        print(diff)

        ans = 0

        for i in worker:
            t = bisect.bisect_right(diff, i)   
            if t == 0:
                continue
            else:
                ans += prefix[t-1]

        return ans
