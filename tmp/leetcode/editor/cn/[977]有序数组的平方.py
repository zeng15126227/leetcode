# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  nums 已按 非递减顺序 排序 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  请你设计时间复杂度为 O(n) 的算法解决本问题 
#  
#  Related Topics 数组 双指针 排序 
#  👍 288 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in nums]
        res_index=len(res)-1

        head=0
        tail=len(res)-1

        while head<=tail:
            if nums[head]**2 <= nums[tail]**2:
                res[res_index] = nums[tail]**2
                tail-=1
            else:
                res[res_index] = nums[head]**2
                head+=1
            res_index-=1

        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().sortedSquares([-4,-1,0,3,10])
    print(res)
