class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(x, k):
            res = ''
            while x > 0:
                res = str(x % k) + res
                x //= k
            return res

        def generate_palindromes(length):
            half = (length + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half
            for i in range(start, end):
                left = str(i)
                if length % 2 == 0:
                    yield int(left + left[::-1])
                else:
                    yield int(left + left[:-1][::-1])

        count = 0
        total = 0
        length = 1

        while count < n:
            for num in generate_palindromes(length):
                if is_palindrome(to_base_k(num, k)):
                    total += num
                    count += 1
                    if count == n:
                        return total
            length += 1

        return total
