class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        i=0
        res=[]
        c=0

        while(i<len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
                if nums[i]==0:
                    c+=1
            if nums[i]==0:
                c+=1
            i+=1
        
        #print(nums)
        i=0

        j=len(nums)-1

        while(i<j):
            while(i<len(nums) and nums[i]!=0):
                i+=1
            
            ch=i
            j=i

            while(j<len(nums) and nums[j]==0):
                j+=1
            
            if ch<j and j<len(nums):
                nums[ch],nums[j]=nums[j],nums[ch]
            else:
                break
        return (nums)

        #return (nums)