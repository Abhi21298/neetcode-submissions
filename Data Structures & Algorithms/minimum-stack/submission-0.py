class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        mins = min(self.minimum[-1], val) if self.minimum else val
        self.minimum.append(mins)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
