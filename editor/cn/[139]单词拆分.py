class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        # #dp[i]表示s[:i]能否被表示
        # dp=[False for _ in range(len(s)+1)]
        # #s=""可以被表示
        # dp[0]=True
        # for i in range(1,len(dp)):
        #     if not dp[i-1]:
        #         continue
        #     for j in range(i,len(dp)):
        #         if s[i-1:j] in wordDict:
        #             dp[j]=True
        # return dp[-1]

        # dp[i]表示s[:i]能否被表示
        dp = [False for _ in range(len(s) + 1)]
        # s=""可以被表示
        dp[0] = True
        for i in range(1, len(dp)):  #遍历背包
            for j in range(i):  #遍历物品，这里物品不是特指字典表里的，而是所有的可分割出来的单词
                word = s[j:i]
                if word in wordDict and dp[j]:
                    dp[i] = True
        return dp[-1]

        # memo = {}
        #
        # def back_track(s):
        #     if s in memo:
        #         return memo[s]
        #     if (not s):
        #         memo[s] = True
        #         return True
        #     for i in range(1, len(s) + 1):
        #         if (s[:i] in wordDict):
        #                 if back_track(s[i:]): return True
        #     memo[s]=False
        #     return False

        return back_track(s)



if __name__ == "__main__":
    res = Solution().wordBreak("leetcode", ["leet", "code"])
    print(res)

