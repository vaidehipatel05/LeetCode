from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char, count in ransom_counter.items():
            if count > magazine_counter[char]:
                return False

        return True