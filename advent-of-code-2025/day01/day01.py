def main():
	
	result1 = 0
	result2 = 0
	curr = 50
    
	with open("input.txt", "r") as file:
		for line in file:
			dir = line[0]
			rot = int(line[1:])
            
			delta = rot if dir == 'R' else -rot
			next_pos = curr + delta
            
			if next_pos % 100 == 0:
				result1 += 1
            
			if dir == 'R':
				added = (next_pos // 100) - (curr // 100)
			else:
				added = ((curr - 1) // 100) - ((next_pos - 1) // 100)
            
			result2 += added
			curr = next_pos

	print(f"Solution for Part 1: {result1}")
	print(f"Solution for Part 2: {result2}")

if __name__ == "__main__":
    main()
