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
            disr(str1 + "(", left - 1, right)
        print(right)
        if right > 0:
            print(right,333)
            disr(str1 + ")", left, right - 1)
        else:
            s = 1
    disr(str1, n, n)
    return res


print(generateParenthesis(2))
# # if 0 <= n <= 8:
# #     left = []
# #     for i in range(1, n + 1):
# #         str1 = i * "(" + (n - i) * ")" #
# #         j = 0
# #         str2 = ""
# #         # print("str1:",str1,2222)
# #         while str1.count("(") > str1.count(")"):
# #             print("str1:", str1)
# #             if str1[j] == "(":
# #                 str2 += ")"
# #                 j += 1
# #             else:
# #                 str2 += "("
# #                 j += 1
# #             print(str2)
# #             if i > n:
# #                 print("str2:", str2)
# #                 break
# #
# #             # print(str1, 3)
# #             break
# #         while str1.count("(") < str1.count(")"):
# #             # print(str1, 2)
# #             break
# #         while str1.count("(") == str1.count(")"):
# #             # print(str1, 1)
# #             break
# #     print(left)
#
# #
# # j = 0
# # r_list1 = []
# # print(str1)
# # while j < n:
# #     if ")" in str1:
# #
# #         j += 1
# #     else:
# #         j += 1
# #         s1 = n * ")"
# #         s2 = str1
# #         s3 = s2 + s1
# #         r_list1.append(s3)
# # print(r_list1)
#
# # for i in r_list:
# #     # print(i)
# #     if i.count(")") > n//2:
# #         print(i)
# #         if ")" in i:
# #             str_1 = i
# #             str_2 = i
# #             for s in i:
# #                 if s == "(":
# #                     str_1 += ")"
# #                     str_2 += "("
# #                 else:
# #                     str_1 += ")"
# #                     str_2 += "("
# #             r_list1.append(str_1)
# #             r_list1.append(str_2)
# #         else:
# #             r_list1.append(i + n * ")")
# #     else:
# #         if ")" in i:
# #             str_1 = i
# #             str_2 = i
# #             for s in i:
# #                 if s == "(":
# #                     str_1 += ")"
# #                     str_2 += "("
# #                 else:
# #                     str_1 += ")"
# #                     str_2 += "("
# #             r_list1.append(str_1)
# #             r_list1.append(str_2)
# #         else:
# #             r_list1.append(i + n * ")")
# # print(r_list)
# # print(r_list1)
# # for num, i in enumerate(r_list):
# #     print(num,i)
# #     while n > num:
#
# # for num, i in enumerate(r_list):
# #     print(num,i)
# #     while n - (num + 1) > 0:
# #         i += len(i) * ")" * (num+1)
# #
# #
# #
# #         j = 0
# #         # i =()
# #
# #
# #
# #         i += (n * 2 - len(i)) // 2 * "()"
# #
# #         r_list[num] = i
# #     print(r_list)
#
# r_list = []
# # str1 = "(" * n + ")" * n
# # r_list.append(str1)
# # j = 0
# # str1 = ""
# # for i in range(n):
# #     str1 += "(" *i
# #     for num in range(i+1):
# #         str1 += ")"
# #     r_list.append(str1)
# #     str1 = ""
# #     print(r_list)
#
# # for i in range(len(str1)):
# #     print(str1)
# #     print(i)
# #     print(j)
# #     if str1[i] == "(":
# #
# #         j = i
# #     elif str1[i] == ")":
# #         str1[j], str1[i] = str1[i], str1[j]
# #         j = i
# #         r_list.append(str1)
# #     # else:
# # print(r_list)
# #
# # i = 0
# # while i < n:
# #     i += 1
# #     print(i)
# # for i in range(1, len(str1)):
# #     # print(i)
# #     if str1[i]=="(":
# #
# #
# #     print(str1[i])
# # print(i)
#
#
#
