from collections import Counter

def get_card_strengths(hand):
    card_strength = {
        'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10,
        '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
        '4': 4, '3': 3, '2': 2
    }
    return tuple(-card_strength[card] for card in hand)

def hand_sort_key(hand):
    hand_rankings = {
        "five_of_a_kind": 1,
        "four_of_a_kind": 2,
        "full_house": 3,
        "three_of_a_kind": 4,
        "two_pair": 5,
        "one_pair": 6,
        "high_card": 7
    }
    hand_type_rank = hand_rankings[get_hand_type(hand)]
    original_order_values = get_card_strengths(hand)
    return (hand_type_rank, original_order_values)

def get_hand_type(hand):
    freq = sorted(Counter(hand).values(), reverse=True)
    count = 0
    for c in hand:
        if c == 'J':
            count += 1
    # print(count)
    if freq == [5]:
        return "five_of_a_kind"
    elif freq == [4, 1]:
        if count == 1 or count == 4:
            return "five_of_a_kind"
        else:
            return "four_of_a_kind"
    elif freq == [3, 2]:
        if count == 2 or count == 3:
            return "five_of_a_kind"
        else:
            return "full_house"
    elif freq == [3, 1, 1]:
        if count == 1 or count == 3:
            return "four_of_a_kind"
        else:
            return "three_of_a_kind"
    elif freq == [2, 2, 1]:
        if count == 1:
            return "full_house"
        elif count == 2:
            return "four_of_a_kind"
        else:
            return "two_pair"
    elif freq == [2, 1, 1, 1]:
        if count == 1 or count == 2:
            return "three_of_a_kind"
        else:
            return "one_pair"
    else:
        if count == 1:
            return "one_pair"
        else:
            return "high_card"

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        hands = []
        bids = {}
        type = []

        for line in file:
            parts = line.split()
            hands.append(parts[0])
            bids[parts[0]] = int(parts[1])

        sorted_hands = sorted(hands, key=hand_sort_key)
        res = 0
        for i, hand in enumerate(sorted_hands):
            res += bids[hand] * (len(sorted_hands) - i)
        print(f"Part 2 solution is {res}")

if __name__ == "__main__":
    main()