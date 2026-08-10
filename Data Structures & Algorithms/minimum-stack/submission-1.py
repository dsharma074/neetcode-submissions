class MinStack:

    def __init__(self):
        self.min = [float("inf")]
        self.arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.min.append(min(val, self.min[-1]))
        

    def pop(self) -> None:
        self.arr = self.arr[:-1]
        self.min = self.min[:-1]
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
