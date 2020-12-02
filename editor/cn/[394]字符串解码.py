class Solution:
    def decodeString(self, s: str) -> str:
        res=''
        stack1=[]
        stack2=[]
        count=0
        for char in s:
            if count==0 and char.isalpha():
                res+=char
            elif char == '[':
                count+=1
                stack1.append(char)
            elif char == ']':
                count-=1
                while stack1[-1] != '[':
                    stack2.append(stack1.pop(-1))
                #'['出栈
                stack1.pop(-1)
                stack2.reverse()
                num = ''
                while stack1 and stack1[-1].isdigit():
                    num=stack1.pop(-1)+num
                t = int(num)*''.join(stack2)
                # 结果一部分
                if count==0:
                    res += t
                elif count>0:
                    stack1+=list(t)
                stack2.clear()
            else:
                stack1.append(char)
        if stack1:
            res+=''.join(stack1)
        return res
if __name__ == "__main__":
    res = Solution().decodeString("3[z]2[2[y]pq4[f]]ef")
    print(res)
