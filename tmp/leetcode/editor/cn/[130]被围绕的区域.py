# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X"
# ,"X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
#  
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 597 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def __init__(self):
        self.dir_x = [0, 1, 0, -1]
        self.dir_y = [1, 0, -1, 0]

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:return board

        m=len(board)
        n=len(board[0])

        #对边缘O进行dfs
        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n or board[x][y]!='O':
                return
            board[x][y]='A'
            for i in range(4):
                dfs(x+self.dir_x[i],y+self.dir_y[i])

        for i in range(0,n):
            dfs(0,i)
            dfs(m-1,i)
        for i in range(0,m):
            dfs(i,0)
            dfs(i,n-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


        return board

# leetcode submit region end(Prohibit modification and deletion)
