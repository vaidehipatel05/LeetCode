class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count1 = 1
        countd1=1
        x=[]
        if all(i == nums[0] for i in nums):
            return 1
            
        for i in range(0,len(nums)-1):
            if nums[i]<nums[i+1]:
                count1 = count1+1
            else:
                x.append(count1)
                count1 = 1
                #print(x)
            x.append(count1)

        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                countd1 = countd1+1
            else:
                x.append(countd1)
                countd1 = 1
                #print("c",x)
            x.append(countd1)
                
        #print(max(x))
        return max(x)