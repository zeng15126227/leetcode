# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  示例: 
# 
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6 
#  Related Topics 栈 数组 哈希表 动态规划 
#  👍 628 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: list) -> int:


        if len(matrix) == 0:
            return 0


        maxarea = 0

        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                #行数据进行填充
                dp[j]=dp[j]+1 if matrix[i][j]=="1" else 0
            maxarea = max(maxarea,self.largestRectangleArea(dp))

        return maxarea

    def largestRectangleArea(self, heights: list) -> int:

        if not heights:
            return 0
        #头尾添加哨兵
        heights = [-1] + heights + [-1]
        res_list = [0 for _ in heights]
        l = len(heights)
        #栈中添加哨兵
        stack = [0]

        for i in range(1,l):
            #栈中元素为递增，下一个元素大于栈顶则入栈
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            #下一个元素小于栈顶，栈顶出栈，出栈的元素左右边界可确定
            elif heights[stack[-1]] > heights[i]:
                while heights[stack[-1]]>heights[i]:
                    out = stack.pop()
                    res_list[out]=(i-stack[-1]-1)*heights[out]
                stack.append(i)
            #下一个元素等于栈顶，栈顶元素进行替换，为了卡住下一个栈元素的左边界
            else:
                stack[-1] = i

        return max(res_list)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    param=[
 ]
    res = Solution().maximalRectangle(param)
    print(res)
