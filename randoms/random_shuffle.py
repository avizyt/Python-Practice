import random
import itertools

FACE_CARD = ("J", "Q", "K", "A")
SUITS = ("H", "D", "C", "S")


def new_deck():
    return [
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARD),
            SUITS,
        )
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()


deck = new_deck()
print("Initial deck: ")
show_deck(deck)

# Shuffle the deck to randomize the order.
random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)


hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())


# Show the hands.
print('\nHands:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()


# Show the remaining deck.
print('\nRemaining deck:')
show_deck(deck)
