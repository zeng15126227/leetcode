# 给出一个以头节点 head 作为第一个节点的链表。链表中的节点分别编号为：node_1, node_2, node_3, ... 。 
# 
#  每个节点都可能有下一个更大值（next larger value）：对于 node_i，如果其 next_larger(node_i) 是 node_j.
# val，那么就有 j > i 且 node_j.val > node_i.val，而 j 是可能的选项中最小的那个。如果不存在这样的 j，那么下一个更大值为 0
#  。 
# 
#  返回整数答案数组 answer，其中 answer[i] = next_larger(node_{i+1}) 。 
# 
#  注意：在下面的示例中，诸如 [2,1,5] 这样的输入（不是输出）是链表的序列化表示，其头节点的值为 2，第二个节点值为 1，第三个节点值为 5 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[2,1,5]
# 输出：[5,5,0]
#  
# 
#  示例 2： 
# 
#  输入：[2,7,4,3,5]
# 输出：[7,0,5,5,0]
#  
# 
#  示例 3： 
# 
#  输入：[1,7,5,1,9,2,5,1]
# 输出：[7,9,9,9,0,5,0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  对于链表中的每个节点，1 <= node.val <= 10^9 
#  给定列表的长度在 [0, 10000] 范围内 
#  
#  Related Topics 栈 数组 链表 单调栈 
#  👍 168 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head: return []

        stack = []
        dic = []
        while (head):
            dic.append(head.val)
            head = head.next

        #结果数组初始化0
        res = []
        for i in range(len(dic)):
            res.append(0)

        for i in range(len(dic)):
            #栈是递增的，每遍历一个元素把栈中小于该节点的节点弹出，写入结果集
            while stack and dic[stack[len(stack) - 1]] < dic[i]:
                idx = stack.pop()
                res[idx]=dic[i]
            #当前节点压站
            stack.append(i)

        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # a = ListNode(10)
    # b = ListNode(10)
    # c = ListNode(7)
    # d = ListNode(2)
    # e = ListNode(6)
    # f = ListNode(2)
    # a.next=b
    # b.next=c
    # c.next=d
    # d.next=e
    # e.next=f
    # res = Solution().nextLargerNodes(a)
    # print(res)
    res = []

    print(res)
