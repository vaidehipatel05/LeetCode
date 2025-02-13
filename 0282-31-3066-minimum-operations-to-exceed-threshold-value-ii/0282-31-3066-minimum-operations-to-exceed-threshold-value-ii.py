class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0

        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            new_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_val)
            count += 1

        return count