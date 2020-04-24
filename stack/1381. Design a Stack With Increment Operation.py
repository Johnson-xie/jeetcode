class CustomStack:
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []
    
    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val

if __name__ == '__main__':
    c = CustomStack(3)
    for i in range(3):
        c.push(i)

    for i in range(3):
        c.push(i)

    c.increment(2, 10)

    for i in range(3):
        c.pop()