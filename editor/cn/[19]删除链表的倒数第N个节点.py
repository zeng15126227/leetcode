# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。 
# 
#  示例： 
# 
#  给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#  
# 
#  说明： 
# 
#  给定的 n 保证是有效的。 
# 
#  进阶： 
# 
#  你能尝试使用一趟扫描实现吗？ 
#  Related Topics 链表 双指针 
#  👍 991 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre=None
        remove=head
        flag=head
        res=None

        for i in range(n-1):
            flag=flag.next
        while flag.next:
            flag=flag.next
            pre=remove
            remove=remove.next
        if pre is None:
            return head.next
        pre.next=remove.next
        return head

    def printNode(self,node:ListNode):
        print(node.val)
        while node.next:
            node=node.next
            print(node.val)





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    res = Solution().removeNthFromEnd(l1,2)
    Solution().printNode(res)