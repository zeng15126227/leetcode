# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  
# 
#  示例 1: 
# 
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。 
# 
#  
# 
#  提示： 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics 排序 数组 
#  👍 645 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: list) -> list:
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda x: x[0])
        merge = []
        merge.append(intervals[0])
        for t in intervals[1:]:
            if merge[-1][1]>=t[0]:
                merge[-1][1] = max(t[1],merge[-1][1])
            else:
                merge.append(t)
        return merge


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
    print(res)