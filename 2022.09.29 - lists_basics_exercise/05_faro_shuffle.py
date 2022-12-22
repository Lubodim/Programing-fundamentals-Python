deck = input().split()
number_of_shuffles = int(input())

half_deck = len(deck) // 2

for shuffle in range(number_of_shuffles):
    new_deck = []
    left_cards = deck[:half_deck]
    right_cards = deck[half_deck:]
    for index_card in range(len(left_cards)):
        new_deck += left_cards[index_card] + right_cards[index_card]
    deck = new_deck
print(deck)