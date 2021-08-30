# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  
#  
#  Related Topics 数组 回溯 
#  👍 990 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n: return []
        res = []
        board = [['.'] * n for _ in range(n)]

        def backtracking(i,board):
            # 终止条件
            if i == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
                return

            # 本层数据集遍历
            for col in range(n):
                if is_valid(i, col, board):
                    board[i][col]='Q'
                    backtracking(i+1,board)
                    board[i][col]='.'


        def is_valid(i, j, board):
            # 检查行，因为遍历本层数据集的时候每一层只会选择一个位置填充Q，所以无需验证
            # 检查列,本身是n，i为剪枝
            for index in range(i):
                if board[index][j] == 'Q':
                    return False
            # 检查135度,剪枝
            row = i
            col = j
            while row>=0 and col>=0:
                if board[row][col] == 'Q':
                    return False
                row-=1
                col-=1
            # 检查45度,剪枝
            row = i
            col = j
            while row >= 0 and col < n:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            return True

        backtracking(0,board)

        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().solveNQueens(8)
    print(res)
