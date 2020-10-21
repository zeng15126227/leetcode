# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
#  Related Topics 堆 链表 分治算法 
#  👍 915 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list) -> ListNode:



        def merge(list,left,right):
            if left==right:
                return list[left]
            mid = (left+right)/2
            merge(list,)




        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            node1 = l1
            node2 = l2
            res = ListNode()
            tmp = res

            while node1 and node2:
                if node1.val < node2.val:
                    tmp.next = node1
                    tmp = tmp.next
                    node1 = node1.next
                else:
                    tmp.next = node2
                    tmp = tmp.next
                    node2 = node2.next
            if node1:
                tmp.next = node1
            if node2:
                tmp.next = node2

            return res.next

        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    left=5
    right=8
    mid = (left + right)//2
    print(mid)
