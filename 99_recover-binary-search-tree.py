# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.x = None
        self.y = None

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            if not self.pre:
                self.pre = node
            else:
                if self.pre.val > node.val:
                    self.y = node
                    print(self.y.val)
                    if not self.x:
                        self.x = self.pre
                        print(self.x.val)
                self.pre = node

            dfs(node.right)

        dfs(root)
        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val
