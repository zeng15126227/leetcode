class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp=[False for _ in s]+[False]
        #s=""可以被表示
        dp[0]=True
        for i in range(1,len(dp)):
            if not dp[i-1]:
                continue
            for j in range(i,len(dp)):
                if s[i-1:j] in wordDict:
                    dp[j]=True
        return dp[-1]



if __name__ == "__main__":
    res = Solution().wordBreak("leetcode", ["leet", "code"])
    print(res)

