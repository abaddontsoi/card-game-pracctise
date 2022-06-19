class card:
    RED = "red"
    BLACK = "black"
    DRAW = "draw"

    def __init__(self, color, point):
        self.color = color
        self.point = point

    def cmp(self, other):
        if other and self.color != other.color:
            # cards are in fight
            return True
        # cards are not in fight
        return False

    def find_winner(self, other):
        if self.cmp(other):
            if self.point > other.point:
                return self
            if self.point < other.point:
                return other
            if self.point == other.point:
                return card.DRAW
        # return none when the point of those cards are equal
        return None

    def __repr__(self) -> str:
        return f"{self.color}_{self.point}"