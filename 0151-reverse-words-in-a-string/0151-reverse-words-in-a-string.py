class Solution:
    def reverseWords(self, s: str) -> str:

     list = []

     list = s.split()

     reversed =list[::-1]
     

     return " ". join(reversed)