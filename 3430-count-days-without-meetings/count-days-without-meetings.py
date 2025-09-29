class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        i=0

        print(meetings)

        while i<len(meetings)-1:
            if  meetings[i][1]>=meetings[i+1][0]:
                ap=[min(meetings[i][0],meetings[i+1][0]),max(meetings[i][1],meetings[i+1][1])]
                meetings.pop(i)
                meetings.pop(i)
                meetings.insert(i,ap)
                #print(meetings)
                i=0
            else:
                i+=1
        
        free=0

        for i in range(len(meetings)-1):
            #print("f")
            free+=(meetings[i+1][0]-meetings[i][1]-1)
        
        #print(meetings)
        
        free+=meetings[0][0]-1
        free+=days-meetings[-1][1]

        return free



        