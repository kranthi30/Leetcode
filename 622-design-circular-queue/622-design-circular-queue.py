class MyCircularQueue:

    def __init__(self, k: int):
        self.buffer = []
        self.limit = k
        

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self.buffer.append(value)
        return True
        

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        self.buffer.pop(0)
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[0]
        

    def Rear(self) -> int:
        if (self.isEmpty()):
            return -1
        return self.buffer[-1]
        

    def isEmpty(self) -> bool:
        if len(self.buffer) == 0:
            return True
        

    def isFull(self) -> bool:
        if len(self.buffer) == self.limit:
            return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()