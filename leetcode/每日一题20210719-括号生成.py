"""22.
括号生成
数字
n
代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且
有效的
括号组合。



示例
1：

输入：n = 3
输出：["((()))",(()()),(())(),()(()),()()()"]
示例
2：

输入：n = 1
输出：["()"]

提示：

1 <= n <= 8
通过次数303, 831
提交次数393, 400
请问您在哪类招聘中遇到此题？
"""


def generateParenthesis(n):
    res = []
    str1 = ""

    def disr(str1, left, right):
        if left == 0 and right == 0:
            res.append(str1)
        if right < left:
            return
        if left > 0:
            print('left',str1,left,right)
            disr(str1 + "(", left - 1, right)
        if right > 0:
            print('right',str1,left,right)
            disr(str1 + ")", left, right - 1)
        print('end', str1, left, right)
    disr(str1, n, n)
    return res


print(generateParenthesis(2))



