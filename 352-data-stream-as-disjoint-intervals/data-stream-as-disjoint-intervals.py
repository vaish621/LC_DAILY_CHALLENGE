class SummaryRanges:

    def __init__(self):
        self.s=set()
        

    def addNum(self, value: int) -> None:
        self.s.add(value)
        

    def getIntervals(self) -> List[List[int]]:
        res=[]

        sort=sorted(self.s)

        for i in sort:
            if res and res[-1][1]+1==i:
                res[-1][1]=i
            else:
                res.append([i,i])
        
        return res
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()