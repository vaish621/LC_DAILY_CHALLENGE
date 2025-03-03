class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        co=0

        for i in nums:
            if i<pivot:
                a.append(i)
            elif i>pivot:
                b.append(i)
            else:
                co+=1
        
        ans=[]
        for i in a:
            ans.append(i)
        
        t=[pivot]*co
        ans.extend(t)

        for i in b:
            ans.append(i)

        return ans

        