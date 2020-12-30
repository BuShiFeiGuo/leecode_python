# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """leecode 230 二叉搜索树中第K小的元素
        利用中序遍历找到第k小的值
        BST 的中序遍历结果是有序的（升序）
        """
        # 记录当前元素的排名
        self.rank = 0
        # 记录结果
        self.res = 0

        def get_k_small(node, k):
            if node is None:
                return
            get_k_small(node.left, k)
            # 中序遍历的位置
            # print(node.val)
            self.rank += 1
            if k == self.rank:
                self.res = node.val
                return
            get_k_small(node.right, k)

        get_k_small(root, k)
        return self.res
