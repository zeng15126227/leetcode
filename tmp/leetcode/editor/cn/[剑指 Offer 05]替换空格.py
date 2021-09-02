# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  Related Topics 字符串 
#  👍 154 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        #计算空格数量
        space_count=0
        for i in s:
            if i == ' ':
                space_count+=1
        #扩展原数组空格数量个大小
        res = list(s)
        res+= [0]*2*space_count
        #两个指针指向新数组末尾和原数组末尾
        first = len(s)-1
        second=len(res)-1
        #从后往前遍历直接覆盖，省去数组移动的时间
        while first>=0:
            if res[first] == ' ':
                res[second] = '0'
                res[second-1]='2'
                res[second-2]='%'
                second=second-3
                first-=1
            else:
                res[second]=res[first]
                second-=1
                first-=1

        return ''.join(res)


        # res=list(s)
        # for i in range(len(s)):
        #     if res[i] == " ":
        #         res[i] = "%2"
        # return ''.join(res)






# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    res = Solution().replaceSpace("We are happy.")
    print(res)
