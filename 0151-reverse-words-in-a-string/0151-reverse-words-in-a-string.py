class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        new_lst = s[::-1]
        return ' '.join(new_lst)