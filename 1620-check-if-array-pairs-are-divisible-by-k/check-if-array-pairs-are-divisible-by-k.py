class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        count=defaultdict(int)

        for i in arr:
            count[i%k]+=1
        
        for i in range(k):
            if i==0:
                if count[i]%2!=0:
                    return False
            else:
                if count[i]!=count[k-i]:
                    return False
        
        return True
        