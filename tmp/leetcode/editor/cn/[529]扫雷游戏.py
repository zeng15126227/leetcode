# 让我们一起来玩扫雷游戏！ 
# 
#  给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）
# 地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。 
# 
#  现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板： 
# 
#  
#  如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。 
#  如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。 
#  如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。 
#  如果在此次点击中，若无更多方块可被揭露，则返回面板。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入: 
# 
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# 输出: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# 解释:
# 
#  
# 
#  示例 2： 
# 
#  输入: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# Click : [1,2]
# 
# 输出: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# 解释:
# 
#  
# 
#  
# 
#  注意： 
# 
#  
#  输入矩阵的宽和高的范围为 [1,50]。 
#  点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。 
#  输入面板不会是游戏结束的状态（即有地雷已被挖出）。 
#  简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 
#  👍 240 👎 0


# leetcode submit region begin(Prohibit modification and deletion)



class Solution(object):

    def __init__(self):
        self.dir_x = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dir_y = [1, 0, -1, 0, 1, -1, 1, -1]


    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        click_x = click[0]
        click_y = click[1]
        if (board[click_x][click_y] == 'M'):
            board[click_x][click_y] = 'X'
        else:
            self.dfs(board, click_x, click_y)
        return board

    def dfs(self,board, x, y):

        cnt = 0
        for i in range(8):
            tx = x + self.dir_x[i]
            ty = y + self.dir_y[i]
            # 坐标超出范围
            if (tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0])):
                continue
            if (board[tx][ty] == 'M'):
                cnt += 1

        if cnt > 0:
            board[x][y] = str(cnt)
        else:
            board[x][y] = 'B'
            for i in range(8):
                tx = x + self.dir_x[i]
                ty = y + self.dir_y[i]
                # 坐标超出范围
                if (tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0])):
                    continue
                if(board[tx][ty]=='E'):
                    self.dfs(board, tx, ty)






# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    param=[['E', 'E', 'E', 'E', 'E'],
           ['E', 'E', 'M', 'E', 'E'],
           ['E', 'E', 'E', 'E', 'E'],
           ['E', 'E', 'E', 'E', 'E']]
    click=[3,0]

    res = Solution().updateBoard(param,click)
    print(res)
