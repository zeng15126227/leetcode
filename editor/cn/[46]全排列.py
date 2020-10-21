# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 922 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: list) -> list:
        res=[]
        lens=len(nums)
        tmp=[]

        def swap(list,a,b):
            tmp = list[a]
            list[a] = list[b]
            list[b] = tmp

        def dfs(start):
            if start==lens:
                res.append(tmp.copy())
                return
            else:
                for i in range(start,lens):
                    tmp.append(nums[i])
                    swap(nums,start,i)
                    dfs(start+1)
                    swap(nums,start,i)
                    tmp.pop()
                return

        dfs(0)






        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().permute([1,2,3])
    print(res)
