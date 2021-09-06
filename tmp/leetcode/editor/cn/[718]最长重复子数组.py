# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。 
# 
#  
# 
#  示例： 
# 
#  输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= len(A), len(B) <= 1000 
#  0 <= A[i], B[i] < 100 
#  
#  Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希 
#  👍 533 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res=0
        m=len(nums1)+1
        n=len(nums2)+1
        #dp[i][j]以表示nums1第i个元素，nums2第j个元素结尾的最长串
        dp = [[0]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    res = max(res,dp[i][j])

        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().findLength([1,2,3,2,1],[3,2,1,4,7])
    print(res)
