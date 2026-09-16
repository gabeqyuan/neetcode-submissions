# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root 
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        if low <= curr.val <= high:
            return curr
        elif curr.val < low:
            return self.lowestCommonAncestor(curr.right, p, q)
        else:
            return self.lowestCommonAncestor(curr.left, p, q)


        