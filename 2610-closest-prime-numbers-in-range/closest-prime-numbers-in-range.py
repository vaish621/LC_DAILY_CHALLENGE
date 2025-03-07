class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        prime=[True]*(right+1)

        prime[0]=prime[1]=False

        for i in range(2,int(right**0.5)+1):
            if prime[i]:
                for j in range(i*i,right+1,i):
                    prime[j]=False
        
        primes=[i for i in range(left,right+1) if prime[i]]

        ma=float('inf')
        res=[-1,-1]
        for i in range(len(primes)-1):
            if abs(primes[i]-primes[i+1])<ma:
                ma=abs(primes[i]-primes[i+1])
                res=[primes[i],primes[i+1]]
        
        return res
