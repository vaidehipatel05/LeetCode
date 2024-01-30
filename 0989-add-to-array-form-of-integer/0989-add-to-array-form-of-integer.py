import sys
sys.set_int_max_str_digits(0)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = [str(i) for i in num]
        res = int("".join(s))
        
        res += k
        res = [int(x) for x in str(res)]
        return res