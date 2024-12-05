def main():

    with open("input.txt", 'r') as file:
        total_scratchcards = 0
        total = 0
        bonus = [1] * 1024
        for line in file:
            hits = 0
            parts = line.split(':')
            game_num = int(parts[0].lstrip("Card: "))
            numbers = parts[1].split('|')
            winning_numbers = list(map(int, numbers[0].split()))
            my_numbers = list(map(int, numbers[1].split()))
            for x in winning_numbers:
                if x in my_numbers:
                    hits += 1
            if hits == 0:
                total_scratchcards += bonus[game_num]
                continue
            total += 2 ** (hits - 1)
            for x in range(hits):
                bonus[game_num + 1 + x] += bonus[game_num]
            total_scratchcards += bonus[game_num]
        print(f"Total points: {total}")
        print(f"Total scratchcards: {total_scratchcards}")

if __name__ == "__main__":
    main()