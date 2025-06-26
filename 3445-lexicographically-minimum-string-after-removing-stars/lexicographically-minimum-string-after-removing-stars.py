class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        d=defaultdict(list)
        re=set()

        for i,ch in enumerate(s):
            if ch!='*':
                d[ch].append(i)
            else:
                #print(d)
                for ch in sorted(d.keys()):
                    if d[ch]:
                        re.add(d[ch].pop())
                        break
        
        ans=''

        for i,ch in enumerate(s):
            if ch!='*' and i not in re:
                ans+=ch
        
        return ans

        