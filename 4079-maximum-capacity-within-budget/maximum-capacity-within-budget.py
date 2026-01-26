import bisect
class Solution(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """

        items=[]

        for i in range(len(costs)):
            items.append([costs[i],capacity[i]])
        
        items.sort()

        ans=0

        pref=[0]*len(costs)
        pref[0]=items[0][1]
        sep=[]
        for i in range(len(items)):
            sep.append(items[i][0])

        i=1
        while i<len(costs):
            pref[i]=max(pref[i-1],items[i][1])
            i+=1
        
        i=0
        print(items)
        print(pref)

        ans=0

        for i in range(len(costs)):
            cost1=items[i][0]
            if cost1<budget:
                ans=max(ans,items[i][1])
            else:
                break
            
            target=budget-cost1
            l=0
            h=i-1
            fi=-1
            while l<=h:
                mid=(l+h)//2
                if items[mid][0]<target:
                    fi=mid
                    l=mid+1
                else:
                    h=mid-1
            
            if fi!=-1:
                ans=max(ans,pref[fi]+items[i][1])
        
        return ans
