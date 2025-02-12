class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        x=-1
        max_arr = {}
        
        for num in nums:
            ni = sum(int(digit) for digit in str(num)) 
            if ni in max_arr:
                x = max(x, num + max_arr[ni])
            max_arr[ni] = max(max_arr.get(ni, 0), num) 
     
        return x