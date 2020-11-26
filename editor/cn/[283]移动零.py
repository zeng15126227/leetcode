class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #把非o元素安相对顺序移动到o元素的前面，每次用第一个0元素和第一个非0元素做交换
        i=-1
        for j in range(len(nums)):
            if not nums[j]==0:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        print(nums)

if __name__ == "__main__":
    list = [0,1,3,0,12]
    Solution().moveZeroes(list)
