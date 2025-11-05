from sortedcontainers import SortedList
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        main=SortedList()
        sec=SortedList()
        tot=0

        def insert(p):
            nonlocal tot
            if len(main)<x or p>main[0]:
                tot+=p[0]*p[1]
                main.add(p)

                if len(main)>x:
                    smallest=main.pop(0)
                    tot-=smallest[0]*smallest[1]
                    sec.add(smallest)
            else:
                sec.add(p)
        
        def remove(p):
            nonlocal tot
            if p in main:
                tot-=p[0]*p[1]
                main.remove(p)
                
                if len(main)<x:
                    if sec:
                        largest=sec.pop(-1)
                        main.add(largest)
                        tot+=largest[0]*largest[1]
            else:
                if p in sec:
                    sec.remove(p)
        
        st=0
        en=0
        d=defaultdict(int)
        ans=[]

        while en<len(nums):

            #element already present in either main or sec gotta remove it
            if d[nums[en]]>0:
                val=d[nums[en]]
                key=nums[en]
                remove((val,key))
            
            d[nums[en]]+=1
            key=nums[en]
            val=d[nums[en]]
            insert((val,key))

            if en-st+1==k:
                ans.append(tot)
                #remove the old one from the list then modify it
                key=nums[st]
                val=d[nums[st]]
                remove((val,key))
                d[nums[st]]-=1
                if d[nums[st]]==0:
                    del d[nums[st]]
                else:
                    key=nums[st]
                    val=d[nums[st]]
                    insert((val,key))
                st+=1
            
            en+=1
        

        return ans
        