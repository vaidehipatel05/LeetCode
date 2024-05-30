class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenw1 = len(word1)
        lenw2 = len(word2)
        
        w3=[]
        i=0
        j=0
        
        while i<lenw1 and j<lenw2:
            w3.append(word1[i])
            w3.append(word2[j])
            i= i+1
            j= j+1
    
                
        while i<lenw1:
            w3.append(word1[i])
            i+=1
        
        while j<lenw2:
            w3.append(word2[j])
            j+=1
            
        return ''.join(w3)