class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        arr.sort()

        mod=pow(10,9)+7

        count={i:1 for i in arr}

        ans=0

        for i in range(1,len(arr)):
            for j in range(0,i):
                if arr[i]%arr[j]==0:
                    l=count[arr[j]]
                    if arr[i]//arr[j] in count:
                        r=count[arr[i]//arr[j]]
                        ans+=(l*r)%mod
                        count[arr[i]]+=(l*r)%mod
        
        return (ans+len(count))%mod
        