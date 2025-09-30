class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        ans=[]

        d=defaultdict(int)
        col=defaultdict(int)

        for i in queries:
            if i[0] not in d:
                d[i[0]]=i[1]
                col[i[1]]+=1
            else:
                col[d[i[0]]]-=1
                if col[d[i[0]]]==0:
                    del col[d[i[0]]]
                d[i[0]]=i[1]
                col[i[1]]+=1
            ans.append(len(col))

        return ans