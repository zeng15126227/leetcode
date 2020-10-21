# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  如果数组中不存在目标值，返回 [-1, -1]。 
# 
#  示例 1: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4] 
# 
#  示例 2: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1] 
#  Related Topics 数组 二分查找 
#  👍 601 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: list, target: int):
        l=0
        r=len(nums)-1

        while l<=r:
            if nums[l] == nums[r]==target:
                while l-1>=0 and nums[l - 1] == nums[l]:
                    l = l - 1
                while r+1<= len(nums)-1 and nums[r + 1] == nums[r]:
                    r = r + 1
                return [l, r]
            mid = (l + r) // 2
            if nums[l] <= target and target <= nums[mid]:
                r=mid
            else:
                l=mid+1
        return [-1,-1]

        # left=0
        # right=0
        # #左边界
        # l=0
        # r=len(nums)-1
        # while l<=r:
        #     mid = (l + r) // 2
        #     if nums[mid]==target:
        #         r=mid-1
        #     elif nums[mid]<target:
        #         l=mid+1
        #     else:
        #         r=mid-1
        # if l<len(nums) and nums[l]==target:
        #     left = l
        # else:
        #     return [-1,-1]
        #
        # #右边界
        # l = 0
        # r = len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         l = mid + 1
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # right=r
        # return [left,right]



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().searchRange([5,7,7,8,8,10],6)
    print(res)

