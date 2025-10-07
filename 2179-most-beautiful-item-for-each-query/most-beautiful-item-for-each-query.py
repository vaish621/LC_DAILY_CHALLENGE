import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        s=sorted(items)

        pref=[0]*len(items)

        pref[0]=(s[0][1])

        for i in range(1,len(s)):
            pref[i]=max(pref[i-1],s[i][1])
        
        ind=[i for i,j in s]
        print(pref)
        ans=[]

        for i in queries:
            t=bisect.bisect_right(ind,i)
            #print(t,i,ind)
            if t==0:
                if ind[t]<=i:
                    ans.append(pref[t])
                else:
                    ans.append(0)
            elif t==len(ind):
                ans.append(pref[t-1])
            else:
                if ind[t]<=i:
                    ans.append(pref[t])
                else:
                    ans.append(pref[t-1])
        
        return ans
        