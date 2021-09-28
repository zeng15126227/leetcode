# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1349 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while (cur):
            # 暂存反转节点下一个节点
            next = cur.next
            #反转链表
            cur.next = pre
            # 更新pre节点
            pre = cur
            # 更新当前节点
            cur = next
        return pre

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":

    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)

    a1.next=a2
    a2.next=a3
    a3.next=a4
    a4.next=a5

    res = Solution().reverseList(a1)
    while res:
        print(res.val)
        res=res.next


