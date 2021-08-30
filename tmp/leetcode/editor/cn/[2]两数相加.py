# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。 
# 
#  请你将两个数相加，并以相同形式返回一个表示和的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每个链表中的节点数在范围 [1, 100] 内 
#  0 <= Node.val <= 9 
#  题目数据保证列表表示的数字不含前导零 
#  
#  Related Topics 递归 链表 数学 
#  👍 6667 👎 0


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
        if not l1 and not l2:
            return 0

        add=0
        res = ListNode(-1)
        tmp= res
        while l1 or l2 or add!=0:
            t_1 = l1.val if l1 else 0
            t_2 = l2.val if l2 else 0
            sum = t_1+t_2+add
            add = sum//10
            val = sum%10
            tmp.next = ListNode(val)
            tmp=tmp.next
            l1 = l1.next
            l2 = l2.next

        return res.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    a.next=b
    b.next=c
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)
    d.next=e
    e.next=f
    res = Solution().addTwoNumbers(a,d)
    print(res.val)