"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
通过次数497,323提交次数949,697
请问您在哪类招聘中遇到此题？
"""


def climb_stairs(n):
    a = b = 1
    for i in range(2, n + 1):
        print('1次', a, ",", b, '=', b, a + b)
        a, b = b, a + b
        print()
        print('2次', a, ",", b, '=', b, a + b)
        print("++++++++++++++++++++++++")
    print(b)
    return b

climb_stairs(3)
