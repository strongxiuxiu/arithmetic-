"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

list1 = ["flower", "flo", "floweight"]


def similar_prefix(x):
    if not x:
        return ""
    res = x[0]  #
    i = 1
    while i < len(x):  # 先确定取出的元素下标是小于x 列表的长度的
        while x[i].find(res) != 0:
            res = res[0:len(res) - 1]
        i += 1
    return res


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    res = ""
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res
