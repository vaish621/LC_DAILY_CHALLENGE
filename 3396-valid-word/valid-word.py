class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n=0
        m=0
        v=0
        c=0

        V=['a','e','i','o','u','A','E','I','O','U']

        for j in word:
            #print(j)
            if j.isalpha():
                if j in V:
                    v=1
                else:
                    c=1
                
            elif j.isdigit():
                continue
            else:
                return False
        
        if len(word)>=3 and v==1 and c==1:
            return True

        return False

        