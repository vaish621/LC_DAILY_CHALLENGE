class Solution:
    def kthCharacter(self, n: int) -> str:

        res=['a']

        for i in range(n-1):
            dp=[]
            for k in res:
                if k=='z':
                    dp.append("a")
                else:
                    dp.append(chr(ord(k)+1))
            res.extend(dp)
            if len(res)>=n:
                break
        
        return res[n-1]
        