class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
      res = []
      max_len= 0

      def removeInvalidParenthesesMethod(s,start,end,temp,count):
          nonlocal res
          nonlocal max_len

          if count<0:
              return
          if start==end:
              if count==0:
                if len(temp)==max_len:
                    res.append(temp)
                    max_len=len(temp)
                elif len(temp)>max_len:
                    res.clear()
                    res.append(temp)
                    max_len = len(temp)
              return


          if s[start]=='(':
              removeInvalidParenthesesMethod(s,start+1,end,temp+'(',count+1)
          elif s[start]==')':
              removeInvalidParenthesesMethod(s, start + 1, end, temp + ')', count -1)
          else:
              removeInvalidParenthesesMethod(s, start + 1, end, temp + s[start], count)

          if s[start]=='(' or s[start]==')':
              removeInvalidParenthesesMethod(s, start + 1, end, temp, count)



      removeInvalidParenthesesMethod(s,0,len(s),'',0)
      return set(res)

if __name__ == "__main__":
    res = Solution().removeInvalidParentheses("(a)())()")
    print(res)
