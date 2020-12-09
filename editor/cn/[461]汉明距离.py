# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。 
# 
#  给出两个整数 x 和 y，计算它们之间的汉明距离。 
# 
#  注意： 
# 0 ≤ x, y < 231. 
# 
#  示例: 
# 
#  
# 输入: x = 1, y = 4
# 
# 输出: 2
# 
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 
# 上面的箭头指出了对应二进制位不同的位置。
#  
#  Related Topics 位运算 
#  👍 357 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # count=0
        # for i in range(32):
        #     mask=1<<i
        #     a=mask & x
        #     b=mask & y
        #     if a!=b:
        #         count+=1
        # return count
        count=0
        xor = x^y
        while xor:
            if xor&1:
                count+=1
            xor = xor >> 1
        return count

        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    Solution().hammingDistance(6,2)
