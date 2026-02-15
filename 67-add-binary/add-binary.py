class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        res = ''
        c = 0
        for i in range(max(len(a), len(b))):  # Corrected range function
            f = ord(a[i]) - ord("0") if i < len(a) else 0
            f1 = ord(b[i]) - ord("0") if i < len(b) else 0
            tot = f + f1 + c
            ch = tot % 2
            res = str(ch) + res
            c = tot // 2
        if c:
            res = "1" + res
        return res          