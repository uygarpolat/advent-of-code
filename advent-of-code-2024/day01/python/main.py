def main():
    list1 = []
    list2 = []

    with open("input.txt", "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)

    similarity_score = sum(list1_element * list2.count(list1_element) for list1_element in list1)

    list1.sort()
    list2.sort()
    
    total_difference = sum(abs(a - b) for a, b in zip(list1, list2))

    print("Total distance is ", total_difference)
    print("Similarity score is: ", similarity_score)

if __name__ == "__main__":
    main()
