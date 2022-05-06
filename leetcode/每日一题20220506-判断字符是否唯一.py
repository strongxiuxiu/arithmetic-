"""
面试题 01.01. 判定字符是否唯一
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。
"""


def simple_find_re_str(s: str):
    res = True
    i = 0
    while i < len(s):
        if s[i] in s[i + 1:]:
            return False
        i += 1
    return res


if __name__ == '__main__':
    print(simple_find_re_str("abc"))
    print(simple_find_re_str("leetcode"))
