# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入： heights = [2,4]
# 输出： 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <=105 
#  0 <= heights[i] <= 104 
#  
#  Related Topics 栈 数组 单调栈 
#  👍 1522 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 单调栈
        stack = []
        res = 0
        #原数组头尾添加哨兵，规避特殊情况判断
        heights.insert(0,0)
        heights.append(0)
        for i in range(len(heights)):
            #减少重复计算
            if stack and heights[stack[-1]] == heights[i]:
                stack[-1]=i
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    height_idx = stack.pop()
                    if stack:
                        w = i - stack[-1] - 1
                        res = max(w * heights[height_idx], res)

                stack.append(i)
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().largestRectangleArea([2,1,2])
    print(res)
