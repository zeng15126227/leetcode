# 在给定的网格中，每个单元格可以有以下三个值之一： 
# 
#  
#  值 0 代表空单元格； 
#  值 1 代表新鲜橘子； 
#  值 2 代表腐烂的橘子。 
#  
# 
#  每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。 
# 
#  返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#  
# 
#  示例 3： 
# 
#  输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 10 
#  1 <= grid[0].length <= 10 
#  grid[i][j] 仅为 0、1 或 2 
#  
#  Related Topics 广度优先搜索 数组 矩阵 
#  👍 400 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):

    def __init__(self):
        self.dir_x = [0, 1, 0, -1]
        self.dir_y = [1, 0, -1, 0]

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        minute = 0
        #记录初始所有腐烂节点  (x,y,minute)
        queue = collections.deque()
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == 2:
                    queue.append((x, y, minute))

        while(queue):
            x,y,min = queue.popleft()
            for i in range(4):
                tx = x+self.dir_x[i]
                ty = y+self.dir_y[i]
                if(0<=tx<m and 0<=ty<n):
                    if (grid[tx][ty] == 1):
                        grid[tx][ty] = 2
                        queue.append((tx, ty, min + 1))
                        minute = max(minute, min + 1)


        if any(1 in row for row in grid):
            return -1

        return minute







# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    data = [[2,1,1],[1,1,0],[0,1,1]]
    res = Solution().orangesRotting(data)
    print(res)

