class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        def rec(i,l):
            if i>=len(arr):
                if len(l)==3:
                    if abs(l[-1]-l[0])<=c:
                        #print(l)
                        return 1
                    else:
                        return 0
                else:
                    return 0
            
            t=0
            nt=0
            if len(l)==0:
                t=rec(i+1,l+[arr[i]])
            elif len(l)==1:
                if abs(arr[i]-l[-1])<=a:
                    t=rec(i+1,l+[arr[i]])
            elif len(l)==2:
                if abs(arr[i]-l[-1])<=b:
                    t=rec(i+1,l+[arr[i]])
            
            nt=rec(i+1,l)

            return t+nt
        
        return (rec(0,[]))
                
        