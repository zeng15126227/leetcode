# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics 数组 矩阵 模拟 
#  👍 468 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)]
        #每一圈的开始坐标
        start_x=0
        start_y=0
        #遍历采用左闭右开，记录每一条边结束的偏移量
        offset=1
        #循环圈数
        loop=n//2
        val=1

        while loop:

            # 从左到右
            for j in range(start_y,n-offset):
                print(start_x,j)
                res[start_x][j]=val
                val+=1
            # 从上到下
            for i in range(start_x,n-offset):
                print(i,n-offset)
                res[i][n-offset]=val
                val += 1
            # 从右到左
            for j in range(n-offset,start_x,-1):
                print(n-offset, j)
                res[n-offset][j]=val
                val += 1
            # 从下到上
            for i in range(n-offset,start_y,-1):
                print(i,start_y)
                res[i][start_y]=val
                val+=1

            start_x+=1
            start_y+=1

            offset+=1
            loop-=1

        if n%2==1:
            mid = n//2
            res[mid][mid]=val

        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().generateMatrix(3)
    print(res)
