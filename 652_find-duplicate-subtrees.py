# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        leecode 652 寻找所有重复的子树
        :param root:
        :return:
        """
        # 保存所有的子树，子树序列化成字符串
        all_trees = set()
        # {子树：重复次数}的字典，子树序列化成字符串
        duplicate_trees = {}

        def get_subtrees(node):
            if node is None:
                return '#'
            left_n = node.left
            right_n = node.right
            left_s = get_subtrees(left_n)
            handle_tree_s(left_s, left_n)
            right_s = get_subtrees(right_n)
            handle_tree_s(right_s, right_n)

            tree_s = str(node.val) + "," + left_s + "," + right_s
            # print(tree_s)
            return tree_s

        def handle_tree_s(tree_s, node):
            if tree_s != '#':
                if tree_s in all_trees:
                    duplicate_trees[tree_s] = node
                else:
                    all_trees.add(tree_s)
        get_subtrees(root)
        # print(duplicate_trees)
        result = list(duplicate_trees.values())
        return result
