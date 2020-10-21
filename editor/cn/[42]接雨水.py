# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1697 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: list) -> int:
        # lens=len(height)
        # res=0
        # max_left=[0 for _ in range(lens)]
        # max_right=[0 for _ in range(lens)]
        # for i in range(1,lens):
        #     max_left[i] = max(max_left[i-1],height[i-1])
        # for i in range(lens-2,-1,-1):
        #     max_right[i] = max(max_right[i + 1], height[i+1])
        #
        # for i in range(1,len(height)-1):
        #     if min(max_left[i],max_right[i])>height[i]:
        #         res+=min(max_left[i],max_right[i])-height[i]
        # return res

        lens = len(height)
        res = 0
        max_left = 0
        max_right = 0
        left=0
        right=lens-1

        while left<=right:
            if max_left<=max_right:
                if max_left<=height[left]:
                    max_left=height[left]
                    left += 1
                else:
                    res+=max_left-height[left]
                    left+=1
            else:
                if max_right<=height[right]:
                    max_right=height[right]
                    right -= 1
                else:
                    res+=max_right-height[right]
                    right-=1

        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().trap([2,0,2])
    print(res)
