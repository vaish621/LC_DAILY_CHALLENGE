class Solution:
    def longestValidParentheses(self, s: str) -> int:

        l=0
        r=0
        ma=0

        for i in s:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            
            if l==r:
                ma=max(ma,l*2)
            
            if r>l:
                r=0
                l=0
        

        t=s[::-1]

        l=0
        r=0

        for j in t:
            if j=='(':
                l+=1
            else:
                r+=1
            
            if l==r:
                ma=max(ma,r*2)
            
            if l>r:
                r=0
                l=0

        return ma
        