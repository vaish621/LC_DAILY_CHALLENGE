class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        t=list(s.split(" "))

        count=0

        for i in t[0]:
            if i in "aeiou":
                count+=1
        
        print(count)
        ans=[t[0]]

        for i in range(1,len(t)):
            cnt=0
            for j in t[i]:
                if j in "aeiou":
                    cnt+=1
            
            if cnt==count:
                ans.append(t[i][::-1])
            else:
                ans.append(t[i])
        
        
        return " ".join(ans)
        