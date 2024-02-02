class Solution:
   def solve(self, text):
      N = ord('z') + ord('a')
      ans=''
      return ans.join([chr(N - ord(s)) for s in text])

ob = Solution()
print(ob.solve("theflagissaywearecrazy"))
print(ob.solve("gsvuoztrhhzbdvzivxizab"))