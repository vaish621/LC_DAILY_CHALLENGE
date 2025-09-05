class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in asteroids:
            if stack:
                if stack[-1]>0 and i<0:
                    if abs(i)==stack[-1]:
                        stack.pop()
                    else:
                        while stack and stack[-1]>0 and -i>stack[-1]:
                            stack.pop()
                        if not stack or stack[-1]<0:
                            stack.append(i)
                        elif stack[-1]==-i:
                            stack.pop()
               
                else:
                    stack.append(i)
            
            else:
                stack.append(i)
            #print(stack)

        return stack


        