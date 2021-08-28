# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/ 
#  Related Topics 数组 回溯 矩阵 
#  👍 395 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board:
            if not word:
                return True
            else:
                return False

        n = len(word)
        flag = False

        def dfs(i, j, k):
            if k == n or flag:
                return True
            x = [1, -1, 0, 0]
            y = [0, 0, 1, -1]
            for index in range(4):
                tx = i + x[index]
                ty = j + y[index]
                if 0<=tx<len(board) and 0<=ty<len(board[0]):
                    if (board[tx][ty] == word[k]):
                        board[tx][ty] = "?"
                        if dfs(tx, ty, k + 1):
                            return True
                        board[tx][ty] = word[k]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    board[i][j] = "?"
                    if dfs(i,j,1):return True
                    board[i][j] = word[0]
        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().exist([["a","a"]],"aaa")
    print(res)
