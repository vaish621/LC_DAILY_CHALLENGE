class Solution:
    def maxOperations(self, s: str) -> int:

        ones=0
        ans=0

        i=0

        while i<len(s):
            if s[i]=='0':
                ans+=ones
                while i<len(s) and s[i]=='0':
                    i+=1
            else:
                ones+=1
                i+=1

        return ans