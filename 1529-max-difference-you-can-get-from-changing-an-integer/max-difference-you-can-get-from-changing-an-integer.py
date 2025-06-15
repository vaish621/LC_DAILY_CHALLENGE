class Solution:
    def maxDiff(self, num: int) -> int:
        num=str(num)
        ma=num

        mi=num

        for d in num:
            if d!='9':
                ma=num.replace(d,'9')
                break
        
        if num[0]!='1':
            mi=num.replace(num[0],'1')
        else:
            for d in num:
                if d!='0' and d!='1':
                    mi=num.replace(d,'0')
                    break
        
        return int(ma)-int(mi)
        