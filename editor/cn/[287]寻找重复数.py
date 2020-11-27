# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出
# 这个重复的数。 
# 
#  示例 1: 
# 
#  输入: [1,3,4,2,2]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [3,1,3,4,2]
# 输出: 3
#  
# 
#  说明： 
# 
#  
#  不能更改原数组（假设数组是只读的）。 
#  只能使用额外的 O(1) 的空间。 
#  时间复杂度小于 O(n2) 。 
#  数组中只有一个重复的数字，但它可能不止重复出现一次。 
#  
#  Related Topics 数组 双指针 二分查找 
#  👍 976 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicate(self, nums: list) -> int:
        #看到有序序列想到二分查找，数字范围在1~也是一种有序
        # l=1
        # h=len(nums)-1
        # while l<h:
        #     mid = (l+h)>>1
        #     cnt=0
        #     for i in nums:
        #         if i <= mid:
        #             cnt += 1
        #     #小于等于mid的数量大于mid，必然有重复
        #     if cnt > mid:
        #         h=mid
        #     else:
        #         l=mid+1
        # return l

        res = 0
        n = len(nums)

        for i in range(32):
            a=0
            b=0
            #01,10,100,1000,10000
            mask=1<<i
            for j in range(n):
                #按位与判断盖位数是否为1
                if nums[j]&mask>=1:
                    a+=1
                #0不包含在1~n-1中，但是0与任何数&结果为0，不影响结果
                if j&mask>=1:
                    b+=1
            #判断该位是否重复，用二进制运算，但是表示出来还是10进制
            #若重复该位为1
            #原数组nums[0]~nums[n-1]中重复的数字，二进制表示中位数为1的位一定会比1~n-1相应位多
            if a>b:
                res = res | mask

        return res

    # leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().findDuplicate([1,3,4,2,2])
    print(res)
