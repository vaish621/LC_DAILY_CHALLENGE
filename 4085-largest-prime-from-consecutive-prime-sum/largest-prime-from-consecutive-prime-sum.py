class Solution:
    def largestPrime(self, n: int) -> int:


        
        

        primes=[2, 5, 17, 41, 197, 281, 7699, 8893, 22039, 24133, 25237, 28697, 32353, 37561, 38921, 43201, 44683, 55837, 61027, 66463, 70241, 86453, 102001, 109147, 116533, 119069, 121631, 129419, 132059, 263171, 287137, 325019, 329401, 333821, 338279, 342761, 360979, 379667, 393961, 398771]


        org=n

        
        l=bisect.bisect_left(primes,org)
        print(l)

        if l==len(primes):
            return primes[l-1]
        
        if primes[l]<=n:
            return primes[l]
        
        if l-1>=0:
            return primes[l-1]
        
        return 0