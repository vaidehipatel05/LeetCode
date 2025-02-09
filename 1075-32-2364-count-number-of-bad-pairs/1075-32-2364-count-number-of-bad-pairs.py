class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        tot = (n * (n - 1)) // 2

        freq = defaultdict(int)
        count = 0

        for i in range(n):
            diff = nums[i] - i
            count += freq[diff]
            freq[diff] += 1
        
        return tot - count 