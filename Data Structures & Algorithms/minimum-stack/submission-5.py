class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.mini == []:
            self.mini.append(val)
        elif self.mini[-1] >= val:
            self.mini.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.mini[-1] == val:
            self.mini.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]