import collections
from collections import deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = collections.Counter(s)

        # Only keep characters that occur at least k times
        valid_chars = []
        for ch in sorted(freq, reverse=True):
            if freq[ch] >= k:
                valid_chars.append(ch)

        # Generate all combinations using BFS
        max_len = len(s) // k
        queue = deque([""])
        ans = ""

        def count_occurrences(sub):
            i = 0
            count = 0
            for ch in s:
                if ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        count += 1
                        i = 0
                        if count >= k:
                            return count
            return count

        while queue:
            cur = queue.popleft()

            for ch in valid_chars:
                new_seq = cur + ch
                if len(new_seq) > max_len:
                    continue
                if count_occurrences(new_seq) >= k:
                    if len(new_seq) > len(ans) or (len(new_seq) == len(ans) and new_seq > ans):
                        ans = new_seq
                    queue.append(new_seq)

        return ans
