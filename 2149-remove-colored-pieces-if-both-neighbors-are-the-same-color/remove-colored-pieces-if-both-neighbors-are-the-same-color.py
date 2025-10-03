class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        al=[]
        bob=[]
        
        for i in range(1,len(colors)-1):
            if colors[i-1]==colors[i] and colors[i]==colors[i+1]:
                if colors[i]=="A":
                    al.append(i)
                else:
                    bob.append(i)
        
        #print(al,bob)

        if len(al)>len(bob):
            return True
        elif len(bob)>len(al):
            return False
        elif len(al)==len(bob):
            return False

        
        