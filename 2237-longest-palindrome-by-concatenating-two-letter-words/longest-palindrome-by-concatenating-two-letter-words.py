class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        di=defaultdict(int)
        ans=0
        

        for i in words:
            if i[::-1] in di and di[i[::-1]]>0:
                ans+=4
                di[i[::-1]]-=1
            else:
                di[i]+=1
        
        for k,v in di.items():
            if v>0 and k[0]==k[1]:
                ans+=2
                break
                
        
        return ans
                
