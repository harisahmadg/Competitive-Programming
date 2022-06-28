from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        sol = []
        self.helper(root, sol)
        print(sol)
        return sol

    def helper(self, root: TreeNode, lst: List[int]):
        
        if root != None:
            self.helper(root.left, lst)
            #print(root.val)
            lst.append(root.val)
            self.helper(root.right, lst)

obj = Solution()
root =  TreeNode(1, right= TreeNode(2))
xd = obj.inorderTraversal(root)