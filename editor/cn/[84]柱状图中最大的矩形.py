# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 
#  👍 959 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        # res=0
        # l=len(heights)
        # for i in range(l):
        #     left=i-1
        #     right=i+1
        #
        #     while right<l and heights[right]>=heights[i]:
        #         right+=1
        #     while left>=0 and heights[left]>=heights[i]:
        #         left-=1
        #     res = max(res, heights[i] * (right - left -1))
        # return res

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
    res = Solution().largestRectangleArea([0,0,0,0,0,0,0,0,2147483647])
    print(res)