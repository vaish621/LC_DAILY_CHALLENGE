class Solution:
    def countGoodNumbers(self,n:int)->int:
        MOD=10**9+7
        
        def mod_pow(base:int,exp:int,mod:int)->int:
            result=1
            base%=mod
            while exp>0:
                if exp&1:
                    result=(result*base)%mod
                base=(base*base)%mod
                exp>>=1
            return result

        even_indices=(n+1)//2
        odd_indices=n//2
        even_part=mod_pow(5,even_indices,MOD)
        odd_part=mod_pow(4,odd_indices,MOD)
        return(even_part*odd_part)%MOD
