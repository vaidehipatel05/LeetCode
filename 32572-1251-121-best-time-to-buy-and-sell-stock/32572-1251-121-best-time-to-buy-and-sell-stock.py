class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_amt = float('inf')
        max_amt = 0
        if not prices:
            return 0
        for price in prices:
            min_amt = min(min_amt, price)
            max_amt = max(max_amt, price - min_amt)

        
        return(max_amt)