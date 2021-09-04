# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。 
# 
#  （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。） 
# 
#  示例 1: 
# 
#  输入: N = 10
# 输出: 9
#  
# 
#  示例 2: 
# 
#  输入: N = 1234
# 输出: 1234
#  
# 
#  示例 3: 
# 
#  输入: N = 332
# 输出: 299
#  
# 
#  说明: N 是在 [0, 10^9] 范围内的一个整数。 
#  Related Topics 贪心 数学 
#  👍 203 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #
        param_list = list(str(n))
        length = len(param_list)
        start = length
        for i in range(length - 1, 0, -1):
            if int(param_list[i]) < int(param_list[i - 1]):
                param_list[i - 1] = str(int(param_list[i - 1]) - 1)
                start = i
        for i in range(start,length):
            param_list[i]='9'
        return int("".join(param_list))


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().monotoneIncreasingDigits(332)
    print(res)
