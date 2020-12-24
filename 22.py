
def draw_card(deck):
    top = deck[0]
    deck.pop(0)
    return top


def round_representation(deck1, deck2):
    return ''.join([str(i) + "," for i in deck1]) + ' ' + ''.join([str(i) + "," for i in deck2])


def game(deck1, deck2, history, task):
    while deck1 and deck2:
        round_repr = round_representation(deck1, deck2)
        if round_repr in history:
            return 1
        history.add(round_repr)

        top1 = draw_card(deck1)
        top2 = draw_card(deck2)
        assert top1 != top2

        winner = 1 if top1 > top2 else 2
        if task == 2 and len(deck1) >= top1 and len(deck2) >= top2:
            winner = game(deck1[:top1], deck2[:top2], set(), task)

        if winner == 1:
            deck1.append(top1)
            deck1.append(top2)
        else:
            deck2.append(top2)
            deck2.append(top1)

    return 1 if deck1 else 2


def play(deck1, deck2, task):
    winning_deck = deck1 if game(deck1, deck2, set(), task) == 1 else deck2
    score = 0
    for i in range(len(winning_deck)):
        score += winning_deck[i] * (len(winning_deck) - i)
    return score


def run():
    with open('input') as file:
        players = file.read().split('\n\n')
        deck1 = list(map(int, players[0].split('\n')[1:]))
        deck2 = list(map(int, players[1].split('\n')[1:]))

        print(play(deck1[:], deck2[:], task=1))
        print(play(deck1[:], deck2[:], task=2))


run()
