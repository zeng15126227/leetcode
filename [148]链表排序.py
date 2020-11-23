# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def find_mid(head):
            if not head or not head.next:
                return head
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            res = slow.next
            slow.next=None
            return res

        def merge(l1,l2):
            head  = cur = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 if l1 else l2
            return head.next

        def sort(head):
            if not head or not head.next:
                return head
            a = find_mid(head)
            right = sort(a)
            b=head
            left = sort(b)
            return merge(left,right)

        return sort(head)

if __name__ == "__main__":
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(3)
    a.next=b
    b.next=c
    c.next=d

    res = Solution().sortList(a)
    print(res)


