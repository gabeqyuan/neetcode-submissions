# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subroot):
            if not root and not subroot:
                return True 
            if not root or not subroot:
                return False
            left = sameTree(root.left, subroot.left)
            right = sameTree(root.right, subroot.right)
            return root.val == subroot.val and left and right 

        def dfs(root, subtree):
            if not root:
                return False
            else:
                return sameTree(root, subtree) or dfs(root.right, subtree) or dfs(root.left, subtree)
        return dfs(root, subRoot)
            
            