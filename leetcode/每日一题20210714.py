"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
通过次数1,082,648提交次数2,887,833
"""


def replace_str(s):
    s_length = len(s)
    if s_length == 0 or s_length == 1:
        return s_length
    str2 = ""  # a
    max_length = 0
    for i in range(s_length):
        if s[i] in str2:
            str_length = len(str2)
            if max_length < str_length:
                max_length = str_length  # 保留目前为止的最大值长度
            if str2[:-1] == s[i]:
                str2 = str2[-1] + s[i]  # 如果最后的字段和拼接的下一段相符合，那就取出最后一个
            else:
                index_num = str2.index(s[i]) + 1
                print(index_num, 444)
                str2 = str2[index_num:] + s[i]
                str2_length = len(str2)
                if max_length < str2_length:
                    max_length = str2_length
        else:
            str2 = str2 + s[i]
            str3_length = len(str2)
            if max_length < str3_length:
                max_length = str3_length
    if 0 <= max_length <= 5 * 104:
        return max_length
    else:
        return 0


str1 = "adsadasdasffdvcvxbfd"

print(replace_str(str1))
