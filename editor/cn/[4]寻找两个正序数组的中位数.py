# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
# 
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法 
#  👍 3087 👎 0



#寻找第k大的数，二分查找
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        # ret = 0.0
        # res = []
        #
        # i = 0
        # j = 0
        # count = 0
        # l=len(nums1)+len(nums2)
        # thr=int(l/2)+1
        # while i < len(nums1) and j < len(nums2) and count<=thr:
        #     if nums1[i] < nums2[j]:
        #         res.append(nums1[i])
        #         i = i + 1
        #     else:
        #         res.append(nums2[j])
        #         j = j + 1
        #     count = count + 1
        # rest=thr-len(res)
        # if i < len(nums1) and rest>0:
        #     res = res + nums1[i:i+rest]
        # if j < len(nums2) and rest>0:
        #     res = res + nums2[j:j+rest]
        #
        # if (l % 2 == 1):
        #     return res[int(l / 2)]
        # else:
        #     return (res[int(l/2)-1]+res[int(l/2)])/2
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.findK(nums1, 0, nums2, 0, left) + self.findK(nums1, 0, nums2, 0, right)) / 2

    def findK(self, nums1, i, nums2, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]

        if k == 1:
            return nums1[i] if nums1[i] < nums2[j] else nums2[j]

        t = k // 2
        v1 = nums1[i + t - 1] if i + t - 1 < len(nums1) else float('inf')
        v2 = nums2[j + t - 1] if j + t - 1 < len(nums2) else float('inf')
        if (v1 < v2):
            return self.findK(nums1, i + t, nums2, j, k - t)
        else:
            return self.findK(nums1, i, nums2, j + t, k - t)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # res = Solution().findMedianSortedArrays([1,3], [2])
    # print(res)
    print(max(100, float('inf')))
