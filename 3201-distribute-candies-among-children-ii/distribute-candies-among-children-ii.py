class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """

        mi=max(0,(n-(2*limit)))
        ma=min(n,limit)
        ans=0

        for i in range(mi,ma+1):
            dn=n-i
            mi2=max(0,dn-limit)
            ma2=min(dn,limit)
            ans+=(ma2-mi2+1)
        

        return ans

        