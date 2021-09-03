# 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。 
# 
# 
#  所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。 
# 
# 
#  
#  例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。 
#  
# 
#  假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# 输出：["JFK","MUC","LHR","SFO","SJC"]
#  
# 
#  示例 2： 
# 
#  
# 输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","
# SFO"]]
# 输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= tickets.length <= 300 
#  tickets[i].length == 2 
#  fromi.length == 3 
#  toi.length == 3 
#  fromi 和 toi 由大写英文字母组成 
#  fromi != toi 
#  
#  Related Topics 深度优先搜索 图 欧拉回路 
#  👍 445 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        #{'JFK': ['KUL', 'NRT', 'NRT'], 'NRT': ['JFK', 'JFK']} 用list作为value，防止处理相同行程问题
        memo={}
        for route in tickets:
            if route[0] in memo:
                memo[route[0]].append(route[1])
            else:
                memo[route[0]]=[route[1]]

        print(memo)
        res=["JFK"]

        def backtracking(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in memo:
                return
            #路径排序
            memo[src].sort()
            for _ in memo[src]:
                #每访问一个目的地，删除元素，防止发生循环行程
                dst = memo[src].pop(0)
                res.append(dst)
                if backtracking(dst):return True
                res.pop()
                memo[src].append(dst)

        backtracking("JFK")
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    print(res)
