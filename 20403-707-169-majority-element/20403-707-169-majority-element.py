class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = -1
        nums.sort()
        x = len(nums)/2
        #print(math.ceil(x))
        res = list(set(nums))
        #print(res)
        
        
        for i in range(len(res)):
            y = nums.count(res[i])
            
            if y>count:
                z = res[i]
                count = y
                #print(z)

        return z
                