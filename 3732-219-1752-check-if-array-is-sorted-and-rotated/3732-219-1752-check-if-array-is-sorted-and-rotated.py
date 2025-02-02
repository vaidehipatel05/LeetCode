class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                print("yes")
            else:
                n=len(nums)-i-1
                #print(n)
                nums = nums[-n:]+nums[:-n]
                i=0
                #print(nums)
                return(all(nums[j] <= nums[j + 1] for j in range(len(nums) - 1)))
        return True