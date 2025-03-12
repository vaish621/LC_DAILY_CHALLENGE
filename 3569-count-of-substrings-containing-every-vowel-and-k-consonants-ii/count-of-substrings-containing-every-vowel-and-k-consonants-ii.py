class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        
        def rec(k):
        
            en=0
            st=0
            vow=0
            ans=0

            d=defaultdict(int)

            while en<len(word):
                if word[en] in 'aeiou':
                    d[word[en]]+=1
                else:
                    vow+=1
                
                while len(d)==5 and vow>=k:
                    ans+=len(word)-en
                    if word[st] in 'aeiou':
                        d[word[st]]-=1
                        if d[word[st]]==0:
                            del d[word[st]]
                    else:
                        vow-=1
                    st+=1
                en+=1
            
            return ans
        
        return abs(rec(k)-rec(k+1))
        




        