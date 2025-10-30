class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        tasks.sort()
        workers.sort()

        def can_assign(mid):
            task=tasks[:mid][::-1]
            worker=workers[-mid:]
            pill=pills

            for t in task:
                if worker and worker[-1]>=t:
                    worker.pop()
                else:
                    if pill==0:
                        return False
                    ind=bisect.bisect_left(worker,t-strength)
                    if ind==len(worker):
                        return False

                    worker.pop(ind)
                    pill-=1

            return True
        
        l=0
        r=min(len(tasks),len(workers))
        ans=0

        while l<=r:
            mid=(l+r)//2
            if can_assign(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        
        return ans


        