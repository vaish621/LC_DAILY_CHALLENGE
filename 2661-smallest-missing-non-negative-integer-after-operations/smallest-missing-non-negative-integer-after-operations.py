class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        d=defaultdict(int)

        for i in nums:
            d[i%value]+=1
        
        mex=0

        while True:
            if mex%value in d:
                d[mex%value]-=1
                if d[mex%value]==0:
                    del d[mex%value]
                mex+=1
            else:
                return mex


        