from functools import lru_cache
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:


        def hamming_distance(w1,w2):
            return sum(i!=j for i,j in zip(w1,w2))
        

        @lru_cache(None)
        def rec(i,prev):

            if i>=len(words):
                return []
            
            best=rec(i+1,prev)
            take=[]

            if prev==-1:
                take=[words[i]]+rec(i+1,i)
                if len(take)>len(best):
                    best=take
            elif groups[prev]!=groups[i] and  len(words[i])==len(words[prev]) and hamming_distance(words[i],words[prev])==1:
                take=[words[i]]+rec(i+1,i)
                if len(take)>len(best):
                    best=take
                
            return best
        
        return rec(0,-1)

            

        