# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = collections.deque()

        q.append((root, root.val))
        good = 1
        while q:
            for i in range(len(q)):
                temp, pathMax = q.popleft()
                if temp.left:

                    if temp.left.val >= pathMax:
                        good += 1
                        

                    q.append((temp.left, max(pathMax, temp.left.val)))

                if temp.right:

                    if temp.right.val >= pathMax:
                        good += 1

                    q.append((temp.right, max(pathMax, temp.right.val)))

            
        return good
                



        