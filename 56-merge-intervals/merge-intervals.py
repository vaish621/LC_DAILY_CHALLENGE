class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        i=0
        intervals.sort(key=lambda x:x[0])
        print(intervals)

        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                mi=min(intervals[i][0],intervals[i+1][0])
                ma=max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i,[mi,ma])
                i=0
            else:
                i+=1
            #print(intervals)

            
        return (intervals)


        