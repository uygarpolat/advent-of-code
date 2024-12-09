def main():
    file_path = "input2.txt"
    with open(file_path, 'r') as file:
        num = file.read()
        num_modified = ''
        index = 0
        for i, c in enumerate(num):
            if i % 2 == 0:
                for j in range(int(c)):
                    num_modified += str(index)
                index += 1
            else:
                for j in range(int(c)):
                    num_modified += '.'
        print(f"{num_modified} before further process")
        i = 0
        while i < len(num_modified):
            # print(num_modified)
            c = num_modified[i]
            if c == '.':
                d = num_modified[len(num_modified) - 1]
                num_modified = num_modified[:i] + d + num_modified[i + 1:]
                num_modified = num_modified[:-1]
                # print(num_modified)
            i += 1

        print(num_modified)

if __name__ == "__main__":
    main()