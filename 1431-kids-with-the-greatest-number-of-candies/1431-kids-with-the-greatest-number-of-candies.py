class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_candies = []
        for i in range(len(candies)):
            temp = extraCandies + candies[i]
            x = max(candies, key=lambda value: int(value))
            if (temp >= x):
                new_candies.append(True)
            else:
                new_candies.append(False)
                
        return new_candies
            