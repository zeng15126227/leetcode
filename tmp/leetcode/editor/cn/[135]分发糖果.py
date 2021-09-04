# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。 
# 
#  你需要按照以下要求，帮助老师给这些孩子分发糖果： 
# 
#  
#  每个孩子至少分配到 1 个糖果。 
#  评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。 
#  
# 
#  那么这样下来，老师至少需要准备多少颗糖果呢？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[1,0,2]
# 输出：5
# 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
#  
# 
#  示例 2： 
# 
#  
# 输入：[1,2,2]
# 输出：4
# 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。 
#  Related Topics 贪心 数组 
#  👍 643 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        g = [1 for _ in ratings]
        # 左到右,得到右边孩子大于左边孩子的情况
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                g[i]=g[i-1]+1
        # 右到左,得到左边孩子大于右边孩子的情况
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                g[i]=max(g[i],g[i+1]+1)
        return sum(g)


# leetcode submit region end(Prohibit modification and deletion)
