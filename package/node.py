class node:
    def __init__(self, el, next=None):
        self.element = el
        self.next = next
    
    def __repr__(self) -> str:
        return f"{self.element} -> {self.next}"