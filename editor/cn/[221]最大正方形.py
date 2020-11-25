class Solution:

    def maximalSquare(self, matrix: list) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        # 初始化dp数组
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]

        # 填充数组
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxSide=max(dp[i][j],maxSide)

        return maxSide*maxSide

if __name__ == "__main__":
    matrix=[["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]]
    res = Solution().maximalSquare(matrix)
    print(res)
