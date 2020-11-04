# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  进阶： 
# 
#  
#  你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 104] 内 
#  -105 <= Node.val <= 105 
#  
#  Related Topics 排序 链表 
#  👍 806 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        len=0
        #求链表长度
        while p:
            len+=1
            p=p.next
        #哨兵
        root = ListNode()
        root.next = head
        #归并规模
        intv=1
        p=root
        cur = root.next
        while intv<len:
            while cur:
                # 第一个链表
                n = intv
                l1 = cur
                while cur and n:
                    cur = cur.next
                    n -= 1
                # 第一个戴合并链表长度未达到规模
                if n:
                    break
                # 第二个链表
                n = intv
                l2 = cur
                while cur and n:
                    cur = cur.next
                    n -= 1
                #l1,l2长度
                c1 = intv
                c2 = intv - n
                #合并
                while c1 and c2:
                    if l1.val<=l2.val:
                        p.next=l1
                        l1=l1.next
                        c1-=1
                    else:
                        p.next=l2
                        l2=l2.next
                        c2-=1
                    p=p.next
                p.next=l1 if c1 else l2
                while c1 or c2:
                    p=p.next
                    c1-=1
                    c2-=1







            intv = intv * 2





        return

# leetcode submit region end(Prohibit modification and deletion)
