class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        x=nums[0]
        ans=x
        for i in range(1,len(nums)):
            if nums[i]> nums[i-1]:
                x=x+nums[i]
            else:
                x=nums[i]
            ans = max(x,ans)
        return(ans)