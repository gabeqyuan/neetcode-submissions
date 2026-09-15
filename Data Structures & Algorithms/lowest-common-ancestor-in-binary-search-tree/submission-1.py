# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        current = root 
        while True:
            if min(p.val, q.val) <= current.val <= max(p.val, q.val):
                break 
            if current.val > max(p.val, q.val):
                current = current.left
            if current.val < min(p.val, q.val):
                current = current.right

            

        return current 

            