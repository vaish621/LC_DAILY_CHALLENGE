class Solution:
    def possibleStringCount(self, word: str) -> int:

        co=0
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                co+=1
        
        return co+1
        