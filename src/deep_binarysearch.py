# let code: maximum depth of binary tree
"""
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
DFS - Depth First Search
BFS - Breadth First Search

"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
print(Solution().maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(Solution().maxDepth(TreeNode(1, TreeNode(0), TreeNode(2))))