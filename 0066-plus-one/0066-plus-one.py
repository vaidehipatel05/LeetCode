class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for num in digits:
            curr = str(num)
            res += curr
        ans = int(res)
        ans +=1
        
        res = [int(x) for x in str(ans)]
        return res
        