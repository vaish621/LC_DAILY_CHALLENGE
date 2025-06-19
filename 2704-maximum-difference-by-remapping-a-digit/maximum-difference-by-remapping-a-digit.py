class Solution:
    def minMaxDifference(self, num: int) -> int:
        o=str(num)
        num=str(num)
        d=''
        d1=''

        for i in num:
            if i!='9':
                o=o.replace(i,'9')
                break

        for i in num:
            if i!='0':
                num=num.replace(i,'0')
                break
        #print(o,num)

        return int(o)-int(num)
