class Solution:
  def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    l=[0]*len(s)

    for i in shifts:
      if i[2]==0:
        l[i[0]]-=1
        if i[1]+1<len(s):
          l[i[1]+1]+=1
      else:
        l[i[0]]+=1
        if i[1]+1<len(s):
          l[i[1]+1]-=1

    #print(l)

    for i in range(1,len(l)):
      l[i]+=l[i-1]

    o=list(s)
    for i in range(len(l)):
        shift = (ord(s[i]) - ord('a') + l[i]) % 26
        o[i] = chr(ord('a') + shift)
    return ''.join(o)
      
        

          
            
