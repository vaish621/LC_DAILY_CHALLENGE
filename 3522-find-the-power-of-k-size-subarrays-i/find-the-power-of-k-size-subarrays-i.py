class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k==1:
            return nums

        st=0
        en=0

        ans=[]
        prev=-1

        while en<len(nums):
            if prev==-1:
                prev=nums[en]
            else:
                if nums[en]!=prev+1:
                    print(st,en)
                    while st<en and st+k<=len(nums):
                        st+=1
                        ans.append(-1)
                    
                else:
                    if en-st+1==k:
                        ans.append(nums[en])
                        st+=1
            
            prev=nums[en]
            #print(prev,en)
            en+=1
        
        
        

        
        
        return ans
                    

        