class MinStack:
    def __init__(self):
        self.stack = []
        self.maxes = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        id_ = len(self.stack)-1
        if id_ == 0:
            self.maxes.append(val)
            self.mins.append(val)
            return

        if val < self.mins[id-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

        if val > self.maxes[id-1]:
            self.maxes.append(val)
        else:
            self.maxes.append(self.maxes[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        self.maxes.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[len(self.stack)-1]