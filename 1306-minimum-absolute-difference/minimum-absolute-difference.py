class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        ans=[]

        arr.sort()

        i=1

        while i<len(arr):
            if len(ans)==0:
                ans.append([arr[i-1],arr[i]])
            else:
                f,l=ans[-1][0],ans[-1][1]
                s=l-f

                if arr[i]-arr[i-1]<s:
                    while len(ans)>0:
                        ans.pop()
                    ans.append([arr[i-1],arr[i]])
                elif arr[i]-arr[i-1]==s:
                    ans.append([arr[i-1],arr[i]])
            i+=1
        
        return (ans)
        