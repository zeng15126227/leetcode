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

class Solution(object):
    # 先遍历物品，再遍历背包
    def test_complete_pack1(self):
        weight = [1, 3, 4]
        value = [15, 20, 30]
        bag_weight = 4

        dp = [0] * (bag_weight + 1)

        for i in range(len(weight)):
            for j in range(weight[i], bag_weight + 1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        print(dp[bag_weight])

        # 先遍历背包，再遍历物品
    def test_complete_pack2(self):
        weight = [1, 3, 4]
        value = [15, 20, 30]
        bag_weight = 4

        dp = [0] * (bag_weight + 1)

        for j in range(bag_weight + 1):
            for i in range(len(weight)):
                if j >= weight[i]:
                    dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        print(dp[bag_weight])


if __name__ == '__main__':
    Solution().test_complete_pack1()
    Solution().test_complete_pack2()