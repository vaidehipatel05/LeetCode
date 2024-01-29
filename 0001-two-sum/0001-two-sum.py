class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_len=len(nums)
        for i in range(sum_len):
            for j in range(i+1, sum_len):
                if( i!=j and nums[i]+nums[j]==target):
                    return [i,j]