# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, high):
            if not root: 
                return True 
            if not (low < root.val < high):
                return False

            #in a binary tree the left node needs to be smaller than the root, but greater than the root's root, and the right node needs to be bigger than the root and bigger than the highest value valid for the root
            return True and dfs (root.left, low, root.val) and dfs(root.right, root.val, high)
            
        return dfs(root, float("-inf"), float("inf")) 
        