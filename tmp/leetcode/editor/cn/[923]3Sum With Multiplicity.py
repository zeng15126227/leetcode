# 给定一个整数数组 A，以及一个整数 target 作为目标值，返回满足 i < j < k 且 A[i] + A[j] + A[k] == target 的
# 元组 i, j, k 的数量。 
# 
#  由于结果会非常大，请返回 结果除以 10^9 + 7 的余数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [1,1,2,2,3,3,4,4,5,5], target = 8
# 输出：20
# 解释：
# 按值枚举（A[i]，A[j]，A[k]）：
# (1, 2, 5) 出现 8 次；
# (1, 3, 4) 出现 8 次；
# (2, 2, 4) 出现 2 次；
# (2, 3, 3) 出现 2 次。
#  
# 
#  示例 2： 
# 
#  输入：A = [1,1,2,2,2,2], target = 5
# 输出：12
# 解释：
# A[i] = 1，A[j] = A[k] = 2 出现 12 次：
# 我们从 [1,1] 中选择一个 1，有 2 种情况，
# 从 [2,2,2,2] 中选出两个 2，有 6 种情况。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= A.length <= 3000 
#  0 <= A[i] <= 100 
#  0 <= target <= 300 
#  
#  Related Topics 数组 哈希表 双指针 计数 排序 
#  👍 78 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumMulti(self, arr, target):

        MOD = 10 ** 9 + 7

        # 排序
        arr.sort()
        res = 0
        length = len(arr)
        i = 0
        while (i < length):
            j = i + 1
            k = length - 1
            r_target = target - arr[i]

            while(j<k):
                if (arr[j] + arr[k] < r_target):
                    j += 1
                elif (arr[j] + arr[k] > r_target):
                    k -= 1
                elif (arr[j] != arr[k]):
                    left, right = 1, 1
                    while (j + 1 < k and arr[j] == arr[j + 1]):
                        j += 1
                        left += 1
                    while (j < k - 1 and arr[k] == arr[k - 1]):
                        k -= 1
                        right += 1
                    res += left * right

                    j+=1
                    k-=1
                else:
                    res += (k - j + 1) * (k - j) / 2

                    break



            i += 1

        return int(res%MOD)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)
    print(res)
