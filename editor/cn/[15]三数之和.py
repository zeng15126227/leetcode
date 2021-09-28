# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2588 👎 0

# -4 -1 -1 0 1 2

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: list) -> list:
        #先排序
        nums.sort()
        n=len(nums)
        i=0
        k=n-1
        result=[]
        #i下标最多n-3
        while i<k:
            #j,k表示双指针起始位置
            j=i+1
            k = n - 1
            while j<k:
                #要使三数之和变小，调整k
                while nums[i]+nums[j]+nums[k]>0 and j<k:
                    k=k-1
                #找到结果
                if nums[i]+nums[j]+nums[k]==0 and j<k:
                    result.append([nums[i],nums[j],nums[k]])
                #要使三数之和变大，调整j
                #注意去重
                j=j+1
                while j < k and nums[j] == nums[j - 1]:
                    j = j + 1
            # 移动第一个指针
            # 注意去重
            i=i+1
            while i<k and nums[i]==nums[i-1]:
                i=i+1
        return result
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    #[-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
    res = Solution().threeSum([-1,0,1,2,-1,-4])
    print(res)
    
