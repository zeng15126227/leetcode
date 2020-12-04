# 给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，
# 则返回 -1.0。 
# 
#  输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"
# ],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 给定：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 返回：[6.0, 0.5, -1.0, 1.0, -1.0 ]
#  
# 
#  示例 2： 
# 
#  输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], que
# ries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]
#  
# 
#  示例 3： 
# 
#  输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["
# a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= equations.length <= 20 
#  equations[i].length == 2 
#  1 <= equations[i][0].length, equations[i][1].length <= 5 
#  values.length == equations.length 
#  0.0 < values[i] <= 20.0 
#  1 <= queries.length <= 20 
#  queries[i].length == 2 
#  1 <= queries[i][0].length, queries[i][1].length <= 5 
#  equations[i][0], equations[i][1], queries[i][0], queries[i][1] 由小写英文字母与数字组成 
#  
#  Related Topics 并查集 图 
#  👍 265 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        #保存父节点
        parents={}
        #保存到父节点权值
        edges={}

        # 寻找根节点
        def find(p):

            if parents[p] != p:
                #路劲压缩
                r = find(parents[p])
                edges[p] = edges[p] * edges[parents[p]]
                parents[p] = r
            return parents[p]

        #初始化节点
        for point in equations:
            a=point[0]
            b=point[1]
            parents[a]=a
            parents[b]=b
            edges[a]=1
            edges[b] = 1
        #合并
        for idx in range(len(equations)):
            a = equations[idx][0]
            b = equations[idx][1]
            ra=find(a)
            rb=find(b)
            parents[ra]=rb
            edges[ra]=values[idx]*edges[b]/edges[a]

        #做查询
        res=[]
        for i in range(len(queries)):
            a=queries[i][0]
            b=queries[i][1]
            if (a not in edges) or (b not in edges) or find(a)!=find(b):
                res.append(-1.0)
            else:
                res.append(edges[a]/edges[b])
        print(parents)
        print(edges)
        return res





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    res = Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],[3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])
    print(res)
