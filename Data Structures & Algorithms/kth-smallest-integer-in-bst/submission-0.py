# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #need to traverse tree in left, node, right format and decrease count everytime we see a node, if count == 0 that is the kth node
        count = k
        result = root.val
        def dfs(node):
            if not node:
                return 
            nonlocal count, result
            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                result = node.val
                return 
            dfs(node.right)
        dfs(root)
        

        return result
            
