def run_hash(hash):
    value = 0
    for c in hash:
        value += ord(c)
        value *= 17
        value %= 256
    return value

def remove_lens(hash, boxes):
    label = hash.rstrip('-')
    box_no = run_hash(label)
    if box_no in boxes:
        labels = boxes[box_no]
        if label in labels:
            index = labels.index(label)
            boxes[box_no].pop(index)
            boxes[box_no].pop(index)
            if not boxes[box_no]:
                del boxes[box_no]

def add_lens(hash, boxes):
    label, foc_len = hash.split('=')
    foc_len = int(foc_len)
    box_no = run_hash(label)
    if not box_no in boxes:
        boxes[box_no] = [label, foc_len]
    else:
        labels = boxes[box_no]
        if label in labels:
            index = labels.index(label)
            boxes[box_no][index + 1] = foc_len
        else:
            boxes[box_no].extend([label, foc_len])

def calculate_score(boxes):
    import math
    score = 0
    for _, box in enumerate(boxes):
        for j in range(0, len(boxes[box]) - 1, 2):
            local_score = (box+1) * math.ceil((j+1) / 2) * boxes[box][j+1]
            score += local_score
    return score

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        hashes = file.readline().strip().split(',')
    num = 0
    for hash in hashes:
        num += run_hash(hash)
    print(f"Solution for Part 1: {num}")

    boxes = {}
    for hash in hashes:
        if '=' in hash:
            add_lens(hash, boxes)
        else:
            remove_lens(hash, boxes)
    score = calculate_score(boxes)
    print(f"Solution for Part 2: {score}")

if __name__ == "__main__":
    main()