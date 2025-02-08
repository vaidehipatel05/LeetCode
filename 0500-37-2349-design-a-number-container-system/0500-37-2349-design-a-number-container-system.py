class NumberContainers:

    def __init__(self):
        self.hm = defaultdict(list)
        self.indexes = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            old_number = self.indexes[index]
            if old_number == number:
                return
                
        self.indexes[index]=number
        heapq.heappush(self.hm[number],index)
        #print(self.indexes)
        

    def find(self, number: int) -> int:
        if number not in self.hm or not self.hm[number]:
            return -1

        
        x = self.hm[number][0]

        if self.indexes.get(x) == number:
                return x
        else:
            heapq.heappop(self.hm[number])
            return self.find(number)

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)