import bisect

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        check = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            check.append(node.val)
            inorder(node.right)

        inorder(root)

        ans = []
        for q in queries:
            idx = bisect.bisect_left(check, q)

            
            if idx < len(check) and check[idx] == q:
                ans.append([q, q])
                continue

           
            floor_val = check[idx - 1] if idx > 0 else -1
            
            ceil_val = check[idx] if idx < len(check) else -1

            ans.append([floor_val, ceil_val])

        return ans
