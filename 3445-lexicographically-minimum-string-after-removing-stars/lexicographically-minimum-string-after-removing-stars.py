from collections import defaultdict, OrderedDict

class Solution:
    def clearStars(self, s: str) -> str:
        d = defaultdict(list)
        to_remove = set()

        for i, ch in enumerate(s):
            if ch != '*':
                d[ch].append(i)
            else:
                for ch in sorted(d.keys()):
                    if d[ch]:
                        to_remove.add(d[ch].pop())
                        break

        res = []
        for i, ch in enumerate(s):
            if i not in to_remove and ch != '*':
                res.append(ch)

        return ''.join(res)
