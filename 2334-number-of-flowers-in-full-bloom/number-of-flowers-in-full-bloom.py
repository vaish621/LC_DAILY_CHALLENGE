import bisect
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        st=[i for i,j in flowers]

        end=[j for i,j in flowers]

        st.sort()
        end.sort()

        ans=[]

        for i in people:
            t=bisect.bisect_right(st,i)
            t1=bisect.bisect_left(end,i)
            ans.append(t-t1)
        
        return ans

