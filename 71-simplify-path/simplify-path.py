class Solution:
    def simplifyPath(self, path: str) -> str:

        parts=path.split('/')
        stack=[]
        for i in parts:
            if i=='..':
                if len(stack)>0:
                    stack.pop()
            elif i and i!='.':
                stack.append(i)
        
        return '/'+'/'.join(stack)

        