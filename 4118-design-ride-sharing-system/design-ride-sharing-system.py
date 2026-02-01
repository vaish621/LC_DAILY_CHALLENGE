class RideSharingSystem(object):

    def __init__(self):
        self.dr=deque()
        self.rid=deque()
        

    def addRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        self.rid.append(riderId)
        

    def addDriver(self, driverId):
        """
        :type driverId: int
        :rtype: None
        """

        self.dr.append(driverId)
        

    def matchDriverWithRider(self):
        """
        :rtype: List[int]
        """
        ans=[]
        if len(self.dr)>0 and len(self.rid)>0:
            t=self.dr.popleft()
            t1=self.rid.popleft()
            ans.append(t)
            ans.append(t1)

            return ans
        
        return [-1,-1]
        

    def cancelRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        if riderId in self.rid:
            self.rid.remove(riderId)
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)