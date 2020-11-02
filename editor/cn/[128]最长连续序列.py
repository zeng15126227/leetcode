class Solution:
    def longestConsecutive(self, nums: list) -> int:
        max_len=0
        tmp_len=0
        for num in nums:
            if num-1 not in nums:
                tmp_len=1
                tmp=num+1
                while tmp in nums:
                    tmp_len+=1
                    max_len=max(max_len,tmp_len)
                    tmp+=1
        return max(max_len,tmp_len)

if __name__ == "__main__":
    res = Solution().longestConsecutive([0])
    print(res)
