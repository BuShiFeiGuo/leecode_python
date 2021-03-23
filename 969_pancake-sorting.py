"""
 核心算法思想是
 1. baseline是如果数组只有一个元素，则不需要翻转
 2. 找到数组中最大值，第一次翻转是将最大值翻转到最上面，第二次翻转是将最大值翻转到最下面。
 3. 重复（递归）第二步，处理cake数组的上面的n-1个cake
 4. 有两个优化点，第二步中，如果最大值在数组的最后一位，不需要后两次翻转，直接处理n-1；如果最大值在第一位，不需要第一次翻转，只需要进行第二次翻转。
"""
class Solution:
    def __init__(self):
        self.sort_idx = []

    def pancakeSort(self, cakes: List[int]) -> List[int]:
        self.sort_idx.clear()

        if len(cakes) == 1:
            return self.sort_idx
        self.cake_sort(cakes, len(cakes) - 1)
        return self.sort_idx

    # 递归处理0-n之间的cake，n-len(cakes)是已经排好序的
    def cake_sort(self, cakes, n):
        # baseline 只要一个元素，不需要翻转
        if n == 0:
            return

        max_idx = self.get_max_cake(cakes, n)
        # 如果最大值就是在最底层(max_idx == n)，则不需要翻转
        if max_idx != n:
            # 如果最大值在第一位（max_idx == 0），则不需要第一次翻转
            if max_idx != 0:
                # 第一次翻转，将最大的cake翻到最上层
                self.reverse(cakes, 0, max_idx)
                self.sort_idx.append(max_idx + 1)
            # 第二次翻转，将最大的cake翻到最下层
            self.reverse(cakes, 0, n)
            self.sort_idx.append(n + 1)
        # 递归处理n-1块cake
        self.cake_sort(cakes, n - 1)

    def get_max_cake(self, cakes, n):
        if n <= 0:
            return 0
        max_cake = -1
        max_cake_idx = 0
        for i in range(n + 1):
            if cakes[i] > max_cake:
                max_cake_idx = i
                max_cake = cakes[i]
        return max_cake_idx

    def reverse(self, cakes, i, j):
        while i < j:
            temp = cakes[i]
            cakes[i] = cakes[j]
            cakes[j] = temp
            i += 1
            j -= 1
        return cakes
