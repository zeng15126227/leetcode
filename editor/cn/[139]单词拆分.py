class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
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

        memo = {}

        def back_track(s):
            if s in memo:
                return memo[s]
            if (not s):
                memo[s] = True
                return True
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                        if back_track(s[i:]): return True
            memo[s]=False
            return False

        return back_track(s)



if __name__ == "__main__":
    res = Solution().wordBreak("leetcode", ["leet", "code"])
    print(res)

