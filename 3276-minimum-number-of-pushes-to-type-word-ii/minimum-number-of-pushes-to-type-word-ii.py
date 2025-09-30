class Solution:
    def minimumPushes(self, word: str) -> int:

        c=collections.Counter(word)

        arr=[]

        for k,v in c.items():
            arr.append(v)
        
        arr.sort(reverse=True)
        

        ans=0

        for i in range(len(arr)):
            ans+=((i//8)+1)*arr[i]
        
        return ans
        