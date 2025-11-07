class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        sadusers=set()

        for u,v in friendships:
            u1=languages[u-1]
            v1=languages[v-1]
            fl=0
            for k in u1:
                if k in v1:
                    fl=1
                    break
            
            if fl==0:
                sadusers.add(u)
                sadusers.add(v)
        
        d=defaultdict(int)
        fr=0
        ma=0

        for i in sadusers:
            lang=languages[i-1]
            for k in lang:
                d[k]+=1
                if d[k]>fr:
                    fr=d[k]
                

        return len(sadusers)-fr
        


        