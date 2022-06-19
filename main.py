from package.card import card
from package.stack import stack
from package.node import node

origin_card_stack = [
    card(card.RED, 4),
    card(card.RED, 3),
    card(card.RED, 2),
    card(card.BLACK, 1),
    card(card.RED, 8),
    card(card.BLACK, 12),
    card(card.BLACK, 6),
    card(card.RED, 0),
]

def main():
    print(origin_card_stack[::-1])
    cardDeck = stack()
    for i in origin_card_stack[::-1]:
        if cardDeck.isEmpty():
            cardDeck.push(i)
        else:
            winner = i.find_winner(cardDeck.peak().element)
            if winner == card.DRAW:
                cardDeck.pop()
            
            while winner is i:
                cardDeck.pop()
                if not cardDeck.isEmpty():
                    winner = i.find_winner(cardDeck.peak().element)
                else:
                    cardDeck.push(i)
                    break

            if winner is None:
                cardDeck.push(i)
        print(cardDeck)
    print(origin_card_stack)

main()