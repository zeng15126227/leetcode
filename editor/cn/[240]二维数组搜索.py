# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
#
#  每行的元素从左到右升序排列。
#  每列的元素从上到下升序排列。
#
#
#  示例:
#
#  现有矩阵 matrix 如下：
#
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
#
#  给定 target = 5，返回 true。
#
#  给定 target = 20，返回 false。
#  Related Topics 二分查找 分治算法
#  👍 483 👎 0
import math

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        max_i = len(matrix)
        max_j = len(matrix[0])

        i = 0
        j = len(matrix[0]) - 1
        while max_i > i >= 0 and max_j > j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False

        #通过二分法把矩阵分成四块，每次可以排除一块，然后在其余三个方块做迭代
        #不同的分法可以简化代码
        # def bin_sch(x_start, x_end, y_start, y_end, target, matrix,min_x,max_x,min_y,max_y):
        #
        #     if min_x > x_start  or x_start >= max_x or \
        #             min_x > x_end  or x_end >= max_x or \
        #             min_y > y_start  or y_start >= max_y or \
        #             min_y > y_end  or y_end >= max_y:
        #         return False
        #
        #     if x_start == x_end and y_start == y_end:
        #         return matrix[x_start][y_start] == target
        #
        #     i = (x_start + x_end)>>1
        #     j = (y_start + y_end)>>1
        #     print(i,",",j)
        #
        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] > target:
        #         return bin_sch(x_start, i-1, y_start, j-1, target, matrix,x_start, i, y_start, j) \
        #                or bin_sch(x_start, i-1, j, y_end, target, matrix,x_start, i, j, y_end+1) \
        #                or bin_sch(i, x_end, y_start, j-1, target, matrix,i, x_end+1, y_start, j)
        #     else:
        #         return bin_sch(x_start, i, j+1, y_end, target, matrix,x_start, i+1, j+1, y_end+1) \
        #                or bin_sch(i+1, x_end, y_start, j, target, matrix,i+1, x_end+1, y_start, j+1) \
        #                or bin_sch(i+1, x_end, j+1, y_end, target, matrix,i+1, x_end+1, j+1, y_end+1)
        #
        # return bin_sch(0, len(matrix)-1, 0, len(matrix[0])-1, target, matrix,0, len(matrix), 0, len(matrix[0]))


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    res = Solution().searchMatrix(matrix, 0)
    print(res)
