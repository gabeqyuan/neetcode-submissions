# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True 
        if not root:
            return True 

        def dfs(node):
            nonlocal isBalanced
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            isBalanced = isBalanced and abs(left - right) <= 1
            return 1 + max(left, right)

        dfs(root)
        return isBalanced