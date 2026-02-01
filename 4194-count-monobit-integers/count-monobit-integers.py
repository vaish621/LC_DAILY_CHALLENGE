class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n==0:
            return 1

        
        o="1"
        ans=1

        while True:
            t1=int(o,2)
            if t1<=n:
                ans+=1
            else:
                break
        
            o+='1'
        
        return ans

            
        