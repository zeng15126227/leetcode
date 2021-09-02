# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针 排序 
#  👍 3657 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        #排序
        nums.sort()

        res = []
        length= len(nums)
        i=0

        while(i<length - 2):
            j=i+1
            k = length - 1
            #剪枝，排序后如果第一个数>0则不可能
            if nums[i]>0:
                break
            while(j<k):
                while (j < k and nums[i] + nums[j] + nums[k] > 0):
                    k = k - 1
                if (j < k and nums[i] + nums[j] + nums[k] == 0):
                    res.append([nums[i],nums[j],nums[k]])
                j = j + 1
                while (j < k and nums[j]==nums[j-1]):
                    j=j+1
            i = i + 1
            while (i<k and nums[i] == nums[i - 1]):
                i = i + 1

        return res








# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    #[-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
    res = Solution().threeSum([-1,0,1,2,-1,-4])
    print(res)
