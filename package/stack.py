from .node import node

class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self) -> str:
        return f"{self.top}"

    def isEmpty(self) -> bool:
        return self.size == 0

    def getSize(self) -> int:
        return self.size
    
    def push(self, el):
        n = node(el, self.top)
        self.top = n
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = self.top.next
            self.size -= 1
            return n
        return None

    def peak(self):
        return self.top