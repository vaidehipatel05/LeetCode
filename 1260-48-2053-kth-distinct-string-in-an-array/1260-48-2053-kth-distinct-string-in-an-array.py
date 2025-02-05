class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a=[]
        b=[]
        for i in range(0,len(arr)):
            for j in range(1,len(arr)):
                if arr[i]==arr[j] and j!=i:
                    #print(arr[i],arr[j])
                    if arr[i] not in a: 
                        a.append(arr[i])
                    #print(a)
        for i in range(0,len(arr)):
            if arr[i] not in a:
                b.append(arr[i])
                #print(b)
                

        #print(b)
        if len(b) >= k:
            return b[k-1]
        else:
            return ""