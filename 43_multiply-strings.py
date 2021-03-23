"""
字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，
返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

算法，采用小学数学的乘法, 哈哈哈哈哈哈
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1_l = list(num1)
        num1_l = [int(i) for i in num1_l]
        num2_l = list(num2)
        num2_l = [int(i) for i in num2_l]
        result = [0] * (len(num1) + len(num2))
        # 逆序遍历，但是index还是从左到右的
        for i in range(len(num1_l)-1, -1, -1):  # 被乘数
            for j in range(len(num2_l)-1, -1, -1):  # 乘数
                temp = num1_l[i] * num2_l[j]
                # 个位
                idx = i + j + 1
                # 十位
                idx2 = i + j
                # 先相加，再进位
                temp += result[idx]
                result[idx] = temp % 10  # 个位直接取余
                # 十位要加到现有十位上，小于10的时候，除法结果是0
                result[idx2] += temp // 10

        # print(result)
        if result[0] == 0:
            result = result[1:]
        re_str = "".join(str(i) for i in result)
        return re_str
