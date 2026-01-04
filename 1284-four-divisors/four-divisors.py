class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0

        for i in nums:
            if i<6:
                continue
            s=i+1
            c=2
            t=int(math.sqrt(i))
            st=2
        
            while  st<=t:
                if i%st==0:
                    rem=i//st
                    if rem!=st:
                        c+=2
                        s+=(st+rem)
                    else:
                        c+=1
                        s+=st
                    if c>4:
                        break
                st+=1
            
            if c==4:
                ans+=s
        
        return ans

            


        