class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        result = 0
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                x=nums[i]*nums[j]
                #results.append((nums[i], nums[j], x))
                product_map[x] += 1
        
        for count in product_map.values():
            if count >= 2:
                result += count * (count - 1) // 2         
        return result*8