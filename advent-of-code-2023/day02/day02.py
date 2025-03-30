
def possible(game_data, builtin):
    flag = 1
    min_red = 0
    min_blue = 0
    min_green = 0
    rounds = next(iter(game_data.values()))
    for data in rounds:
        if data.get('blue', 0) > builtin[0].get('blue', 0):
            flag = 0
        if min_blue < data.get('blue', 0):
            min_blue = data.get('blue', 0)
        if data.get('red', 0) > builtin[0].get('red', 0):
            flag = 0
        if min_red < data.get('red', 0):
            min_red = data.get('red', 0)
        if data.get('green', 0) > builtin[0].get('green', 0):
            flag = 0
        if min_green < data.get('green', 0):
            min_green = data.get('green', 0)
    return flag, min_blue * min_green * min_red

def main():
    total_required_balls = 0
    res = 0
    line_num = 0
    total = 0
    builtin = [{'blue': 14, 'red': 12, 'green': 13}]
    game_data = {}
    with open("input.txt", "r") as file:
        for line in file:
            line_num, temp = line.removeprefix("Game ").split(":", 1)
            temp = temp.strip()
            rounds = temp.split(';')
            parsed_rounds = []

            for rnd in rounds:
                items = rnd.strip().split(',')
                round_dict = {}
                for item in items:
                    value, color = item.strip().split(' ', 1)
                    round_dict[color] = int(value)
                parsed_rounds.append(round_dict)
            
            current_game_data = {line_num: parsed_rounds}
            game_data[line_num] = parsed_rounds
            flag, res = possible(current_game_data, builtin)
            if flag > 0:
                total += int(line_num)
            total_required_balls += res
    print(f"Sum of possible games is {total}")
    print(f"Sum of minimal game count is {total_required_balls}")

if __name__ == "__main__":
    main()
