class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {2: "abc", 3: "def", 4: "ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        if digits == "":
            return []
            
        dig = list(map(int, digits))  
        x=[]
        
        for i in range(len(dig)):
            #print(dig[i])
            x.append(my_dict[dig[i]])

        result = [''.join(pair) for pair in itertools.product(*x)]
        
        return result