class Solution:
    def kthCharacter(self, k: int) -> str:

        b=['a']
        if len(b)==k:   
            return b[-1]

        while True:
            ans=''
            for i in b:
                v=ord(i)+1
                ch=chr(v)
                ans+=ch
            for j in ans:
                b.append(j)
                if len(b)==k:   
                    return b[-1]
        
        # print(b)
        # return b[-1]

        