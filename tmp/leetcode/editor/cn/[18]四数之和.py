# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b
# ], nums[c], nums[d]] ： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 双指针 排序 
#  👍 932 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        res=[]

        i=0
        while i < n-3:
            j=i+1
            while j < n-2:
                k=j+1
                z=n-1
                while k<z:
                    while k<z and nums[i]+nums[j]+nums[k]+nums[z]>target:
                        z-=1
                    if k<z and nums[i]+nums[j]+nums[k]+nums[z]==target:
                        res.append([nums[i],nums[j],nums[k],nums[z]])
                    k=k+1
                    while k<z and nums[k]==nums[k-1]:
                        k+=1
                j+=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
            i+=1
            while i<j and nums[i]==nums[i-1]:
                i+=1

        return res




# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().fourSum([1,0,-1,0,-2,2],0)
    print(res)
