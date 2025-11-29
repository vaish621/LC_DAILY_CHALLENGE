class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        count=collections.Counter(s)
        sort=sorted(count.keys())

        def fill_freely(res):

            for ch in sort:
                for _ in range(count[ch]):
                    res.append(ch)
            
            return "".join(res)
        

        def rec(pos,ans,isTight):
            
            if len(ans)==len(s):
                ch="".join(ans)
                if ch and ch>target:
                    return ch
                return False
            
            for ch in sort:
                if count[ch]==0:
                    continue
                
                if ch<target[pos]:
                    continue
                elif ch>target[pos]:
                    count[ch]-=1
                    return fill_freely(ans+[ch])
                else:
                    count[ch]-=1
                    check=rec(pos+1,ans+[ch],True)

                    if check!=False:
                        return check
                    
                    count[ch]+=1
            
            return False
        
        ans = (rec(0,[],True))

        if not ans:
            return ""
        
        return ans


        