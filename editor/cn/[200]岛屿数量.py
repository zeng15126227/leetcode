# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 864 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: list) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    #计数器+1
                    count+=1
                    #遍历相邻节点
                    stack=[]
                    stack.append((i,j))
                    while stack:
                        #访问过后重置为0
                        x,y=stack.pop(0)
                        grid[x][y]=0
                        if 0<=x<m and 0<=y-1<n and grid[x][y - 1] == "1":
                            grid[x][y - 1] = 0
                            stack.append((x,y-1))
                        if 0<=x<m and 0<=y+1<n and grid[x][y + 1] == "1":
                            grid[x][y + 1] = 0
                            stack.append((x,y+1))
                        if 0<=x-1<m and 0<=y<n and grid[x - 1][y] == "1":
                            grid[x - 1][y] = 0
                            stack.append((x-1,y))
                        if 0<=x+1<m and 0<=y<n and grid[x + 1][y] == "1":
                            grid[x + 1][y] = 0
                            stack.append((x+1,y))

        return count


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
         ]
    res = Solution().numIslands(grid)
    print(res)
