def one_more_chance(report, index, num):

    new_report = report[:]
    new_report2 = report[:]

    del new_report[index]
    del new_report2[index + 1]
    if (num > 0):
        increasing = all(0 < new_report[i+1] - new_report[i] <= 3 for i in range(len(new_report) - 1))
        increasing2 = all(0 < new_report2[i+1] - new_report2[i] <= 3 for i in range(len(new_report2) - 1))
        if (increasing or increasing2):
            return 0
        return 1
    else:
        decreasing = all(0 < new_report[i] - new_report[i+1] <= 3 for i in range(len(new_report) - 1))
        decreasing2 = all(0 < new_report2[i] - new_report2[i+1] <= 3 for i in range(len(new_report2) - 1))
        if (decreasing or decreasing2):
            return 0
        return 1

def main():
    counter = 0
    with open("input.txt", "r") as file:
        for line in file:
            data = list(map(int, line.split()))
            new_data = data
            new_data2 = data
            for i in range(len(data) - 1):
                if (data[i + 1] > data[i] and data[i + 1] - data[i] <= 3):
                    continue
                else:
                    counter -= one_more_chance(new_data, i, 1)
                    break
            counter += 1
            for i in range(len(data) - 1):
                if (data[i + 1] < data[i] and data[i] - data[i + 1] <= 3):
                    continue
                else:
                    counter -= one_more_chance(new_data2, i, -1)
                    break
            counter += 1
        print(counter)
if __name__ == "__main__":
    main()