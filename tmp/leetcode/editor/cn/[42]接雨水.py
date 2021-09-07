# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  0 <= n <= 3 * 104 
#  0 <= height[i] <= 105 
#  
#  Related Topics 栈 数组 双指针 动态规划 单调栈 
#  👍 2652 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 双指针
        # res = 0
        # for i in range(1,len(height)-1):
        #     l = i
        #     r = i
        #     for x in range(i - 1, -1, -1):
        #         if height[x] > height[l]:
        #             l = x
        #     for y in range(i + 1, len(height)):
        #         if height[y] > height[r]:
        #             r = y
        #     res += min(height[l], height[r]) - height[i]
        # return res

        # 动态规划
        # # dp_left[i]:i左边最大高度
        # # dp_right[i]:i右边最大高度
        # dp_left = [0] * len(height)
        # dp_right = [0] * len(height)
        # # 计算dp数组
        # dp_left[0] = height[0]
        # for i in range(1, len(height)):
        #     dp_left[i] = max(dp_left[i - 1], height[i])
        # dp_right[len(height) - 1] = height[len(height) - 1]
        # for i in range(len(height) - 2, -1, -1):
        #     dp_right[i] = max(dp_right[i + 1], height[i])
        # #计算每个点的值
        # res = 0
        # for i in range(1, len(height) - 1):
        #     res += min(dp_left[i], dp_right[i]) - height[i]
        #
        # return res

        # 单调栈，保存下标
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                #获取底的值
                bottom = height[stack.pop()]
                if stack:
                    #长方形宽度
                    w = i-stack[-1]-1
                    #深度*宽度
                    res+=(min(height[i],height[stack[-1]])-bottom)*w
            stack.append(i)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(res)
