class Solution:
    def checkPowersOfThree(self, n: int) -> bool:


        def rec(i,t):
            #print(t)
            if i>16:
                return False
            if t>n:
                return False
            
            if t==n:
                #print(t)
                return True
            tt=False
            nt=False
            if t+pow(3,i)>n:
                return
            else:
                tt=rec(i+1,t+pow(3,i))
            nt=rec(i+1,t)

            return tt or nt
        
        ans=(rec(0,0))
        if ans==None or False:
            return False
        else:
            return True
        