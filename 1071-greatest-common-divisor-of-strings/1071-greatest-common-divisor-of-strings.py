class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2+str1:
            return ""
        
        def gdc(a,b):
            while b:
                a,b = b, a%b
            return a
        
        gdclen= gdc(len(str1), len(str2))
        
        return str1[:gdclen]