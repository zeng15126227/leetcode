# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须原地修改，只允许使用额外常数空间。 
# 
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
# 1,2,3 → 1,3,2 
# 3,2,1 → 1,2,3 
# 1,1,5 → 1,5,1 
#  Related Topics 数组 
#  👍 672 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        n=length-1
        while n>0 and nums[n]<=nums[n-1]:
            n-=1
        if n==0:
         nums[:] = nums[::-1]
        else:
            i=n-1
            j=n
            while j<length and nums[j]>nums[i]:
                j+=1
            self.swap(nums,i,j-1)
            nums[:] = nums[:i+1]+nums[i+1:][::-1]



    def swap(self,nums,i,j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    a = [2,3,1]
    Solution().nextPermutation(a)
    print(a)
