# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法 
#  👍 653 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: list, word: str) -> bool:

        direction = [(0,1),(0,-1),(1,0),(-1,0)]


        m=len(board)
        n=len(board[0])
        visited = set()

        def check(i,j,k):
            if board[i][j] != word[k]:
                return False
            if k==len(word)-1:
                return True

            visited.add((i,j))
            for (x,y) in direction:
                newi=i+x
                newj=j+y
                if 0<=newi<m and 0<=newj<n:
                    if (newi,newj) not in visited:
                        if check(newi,newj,k+1):
                            return True
            visited.remove((i,j))
            return False


            return True


        for i in range(m):
            for j in range(n):
                if check(i,j,0):
                    return True

        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    board =[
       ['A','B','C','E'],
       ['S','F','C','S'],
       ['A','D','E','E']
     ]
    word="ABCB"
    res = Solution().exist(board,word)
    print(res)

