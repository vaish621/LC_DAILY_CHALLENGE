class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        if k==1:
            return 'a'

        nk=-1
        op=-1

        le=1

        for i in range(len(operations)):
            le*=2
            if le>=k:
                nk=k-(le//2)
                op=operations[i]
                break
        
        ch=self.kthCharacter(nk,operations)


        if op==0:
            return ch
        else:
            if ch=='z':
                return 'a'
            o=ord(ch)+1
            return chr(o)

        