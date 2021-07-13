"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]


提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
通过次数618,613提交次数932,989
"""


class Node:
    # 这是一个单向链表
    def __init__(self, item):
        self.next = None  # 这里指向下一个元素节点
        self.data = item  # 这里代表该节点的值


class LinkList:
    def __init__(self):
        self.header = None
        self.length = 0

    def is_empty(self):
        if self.header == 0:
            return False
        else:
            return True

    def add_item(self, node):
        if self.header:
            self.header = node
            self.length += 1


node1 = Node('name')
print(Node('name'))

link_list = LinkList()
link_list.add_item(node1)
print(link_list.length, link_list.header)
