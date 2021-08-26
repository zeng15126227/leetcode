# 给定一个单链表 L 的头节点 head ，单链表 L 表示为： 
# 
#  L0 → L1 → … → Ln-1 → Ln 
# 请将其重新排列后变为： 
# 
#  L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … 
# 
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: head = [1,2,3,4]
# 输出: [1,4,2,3] 
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: head = [1,2,3,4,5]
# 输出: [1,5,2,4,3] 
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 5 * 104] 
#  1 <= node.val <= 1000 
#  
#  Related Topics 栈 递归 链表 双指针 
#  👍 652 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:return None


        #寻找链表中点
        def get_mid(head):
            fast = head
            slow = head
            while (fast.next and fast.next.next):
                slow = slow.next
                fast = fast.next.next
            return slow


        #链表反转
        def reverse(head):
            cur = head
            pre = None
            while (cur):
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre


        #链表合并
        def merge(l1,l2):
            while(l1 and l2):
                t1 = l1.next
                t2 = l2.next

                l1.next = l2
                l1 = t1

                l2.next = t1
                l2 = t2



        mid = get_mid(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = reverse(l2)
        merge(l1, l2)












# leetcode submit region end(Prohibit modification and deletion)
