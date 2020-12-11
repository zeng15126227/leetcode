# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表 
#  👍 711 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums:list, k: int) -> int:
        #i~j的和可以通过0~j的和减去0~i-1的和得到
        mp={}
        #压入初始值
        mp[0]=1
        #记录0~i的前缀和
        pre=0
        #记录符合条件的数量
        count=0

        for i in nums:
            #更新pre
            pre+=i
            #判断是否存在pre-k的前缀和存在
            count+=mp.get(pre-k,0)
            # 更新mp
            mp[pre] = mp.get(pre, 0) + 1
        return count



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res=Solution().subarraySum([1],0)
    print(res)
