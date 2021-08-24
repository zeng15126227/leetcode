# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,5,6,4]
# 输出: 5 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序 
#  👍 503 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0

        tmp = []
        length=len(nums)
        return self.recurPair(nums, 0, length-1, tmp)

    def recurPair(self, nums, left, right, tmp):

        if left==right:return 0

        # 解决数值过大，超出范围的问题
        mid = left + (right - left) // 2

        count_left = self.recurPair(nums, left, mid, tmp)
        count_right = self.recurPair(nums, mid + 1, right, tmp)
        count_merge = self.mergePair(nums, left, mid,right, tmp)

        return   count_left+count_right+count_merge

    def mergePair(self,nums, left, mid,right, tmp):

        tmp[left:right + 1] = nums[left:right + 1]

        i = left
        j = mid + 1
        count=0

        for k in range(left,right+1):
            if (i > mid and j <= right):
                nums[k] = tmp[j]
                j += 1
            elif (i <= mid and j > right):
                nums[k] = tmp[i]
                i += 1
            elif (tmp[i] <= tmp[j]):
                nums[k] = tmp[i]
                i += 1
            else:
                nums[k] = tmp[j]
                count += mid - i + 1
                j += 1

        return count

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().reversePairs([7,5,6,4])
    print(res)