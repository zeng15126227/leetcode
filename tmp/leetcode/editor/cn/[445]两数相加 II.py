# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数字都不会以零开头。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
#  
# 
#  示例2： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
#  
# 
#  示例3： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 100] 
#  0 <= node.val <= 9 
#  输入数据保证链表代表的数字无前导 0 
#  
# 
#  
# 
#  进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。 
#  Related Topics 栈 链表 数学 
#  👍 416 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []

        while (l1):
            s1.append(l1.val)
            l1 = l1.next
        while (l2):
            s2.append(l2.val)
            l2 = l2.next

        res = None
        add = 0
        while (s1 or s2 or add != 0):
            l = 0 if not s1 else s1.pop()
            r = 0 if not s2 else s2.pop()
            sum = l + r + add
            add = sum // 10
            val = sum % 10
            node = ListNode(val)
            node.next = res
            res = node

        return res

# leetcode submit region end(Prohibit modification and deletion)
