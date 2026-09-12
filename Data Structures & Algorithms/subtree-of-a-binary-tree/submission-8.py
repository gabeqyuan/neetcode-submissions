# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(tree, subtree):
            if not tree and not subtree:
                return True
            if not tree or not subtree:
                return False
            left = sameTree(tree.left,  subtree.left)
            right = sameTree(tree.right,  subtree.right)
            return tree.val == subtree.val and left and right 
        
        def dfs(root, subroot):
            if not root:
                return False
            else:
                return sameTree(root, subroot) or dfs(root.right, subroot) or dfs(root.left, subroot)
                
        
        return dfs(root, subRoot)

            
            
            