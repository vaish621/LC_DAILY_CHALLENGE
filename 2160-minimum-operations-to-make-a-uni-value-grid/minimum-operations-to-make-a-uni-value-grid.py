class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        nums=[]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])
        
        nums.sort()

        median=nums[len(nums)//2]
        
        count=0

        for i in nums:
            if i==median:
                continue
            
            check=abs(median-i)

            if check%x!=0:
                return -1
            else:
                count+=check//x
            
        
        return count
        

        