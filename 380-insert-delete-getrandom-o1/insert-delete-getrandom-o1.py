import random
class RandomizedSet:

    def __init__(self):

        self.ar=[]
        self.ind={}
        
        

    def insert(self, val: int) -> bool:
        if val in self.ind:
            return False
        
        self.ar.append(val)
        self.ind[val]=len(self.ar)-1
        
        return True
        

        

    def remove(self, val: int) -> bool:

        if val not in self.ind:
            return False
        
        idx=self.ind[val]
        la=self.ar[-1]

        #print(self.ar)

        self.ar[idx],self.ar[-1]=self.ar[-1],self.ar[idx]

        self.ind[la]=idx

        self.ar.pop()

        del self.ind[val]

        return True

    def getRandom(self) -> int:

        val=random.choice(self.ar)

        return val

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()