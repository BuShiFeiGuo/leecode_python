"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

贪心算法，是动规的一种特殊形式，需要满足的条件更多
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        farthest = 0
        end = 0
        for i in range(len(nums) - 1):
            num = nums[i]
            farthest = max(num + i, farthest)

            # 每一次跳跃的边界
            if end == i:
                step += 1
                # 更新边界
                end = farthest
            # if farthest >= len(nums):
                # 不能加这个判断？
            #     return step

        return step


if __name__ == '__main__':
    solution = Solution()
    # mylist = [2, 3, 1, 1, 4]
    mylist = [1,2,3,4,5]
    print(solution.jump(mylist))
