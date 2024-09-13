class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        num_new = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                num_new.append(nums[i])
        for i in range(count):
            num_new.append(0)
        for i in range(len(num_new)):
            nums[i] = num_new[i]