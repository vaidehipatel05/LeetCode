class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t=''.join(sorted(t))
        s=''.join(sorted(s))
        if s==t:
            return True
        else:
            return False