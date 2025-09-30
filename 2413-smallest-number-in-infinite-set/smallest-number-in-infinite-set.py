class SmallestInfiniteSet:

    def __init__(self):
        self.d={i:True for i in range(1,1002)}
        self.small=1

        

    def popSmallest(self) -> int:
        if self.d[self.small]:
            self.d[self.small]=False
            i=self.small
            while i<1001 and not self.d[i]:
                i+=1
            temp=self.small
            self.small=i
            return temp
        else:
            i=self.small

            while i<1001 and not self.d[i]:
                i+=1
            self.d[i]=False
            self.small=i+1
            return i

        

    def addBack(self, num: int) -> None:
        self.d[num]=True
        self.small=1
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)