class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def merge(l1,l2):

            i=0
            j=0
            add=[]

            while i<len(l1) and j<len(l2):
                if l1[i]<l2[j]:
                    add.append(l1[i])
                    i+=1
                else:
                    add.append(l2[j])
                    j+=1
            
            while i<len(l1):
                add.append(l1[i])
                i+=1
            
            while j<len(l2):
                add.append(l2[j])
                j+=1
            
            if len(add)%2!=0:
                return add[len(add)//2]/1
            else:
                return (add[len(add)//2]+add[(len(add)//2)-1])/2
        

        return merge(nums1,nums2)



        