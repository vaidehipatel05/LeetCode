class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = set()
        j=0
        count = 0

        for i in range(0,len(s)):
            while s[i] in k:
                k.remove(s[j])
                j=j+1

            k.add(s[i])
            count = max(count, i-j+1)
        return count