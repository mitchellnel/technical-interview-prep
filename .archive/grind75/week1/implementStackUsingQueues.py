class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if len(self.output) == 0:
            while len(self.input) > 0:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
