def main():
    regs_and_pros = ([37293246,0,0], (2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0)), ([729,0,0], (0,1,5,4,3,0)), ([0,0,9], (2,6)), ([10,0,0], (5,0,5,1,5,4)), ([100,4,0], (0,5)), ([117440,0,0], (0,3,5,4,3,0))
    regs, progs = regs_and_pros[0]
    # print(regs, progs)
    solution_1 = ""

    func = [ins0, ins1, ins2, ins3, ins4, ins5, ins6, ins7]

    prog = 0
    while(prog < len(progs)):
        if prog < 0:
            continue
        opcode = progs[prog]
        operant = progs[prog+1]

        res, solution_1 = func[opcode](regs, operant, solution_1)
        if res:
            prog = operant - 2
        prog += 2

    solution_1 = solution_1[1:]
    # print(regs, progs)
    print(f"Solution for Part 1: {solution_1}")

def ins0(regs, operant, solution):
    numerator = regs[0]
    combo_operant = get_combo_operant(regs, operant)
    denominator = 2 ** combo_operant
    regs[0] = numerator // denominator
    return 0, solution

def ins1(regs, operant, solution):
    regs[1] ^= operant
    return 0, solution

def ins2(regs, operant, solution):
    combo_operant = get_combo_operant(regs, operant)
    regs[1] = combo_operant % 8
    return 0, solution

def ins3(regs, operant, solution):
    if regs[0] != 0:
        return 1, solution
    return 0, solution

def ins4(regs, operant, solution):
    regs[1] ^= regs[2]
    return 0, solution

def ins5(regs, operant, solution):
    combo_operant = get_combo_operant(regs, operant)
    solution = solution + ',' + str(combo_operant % 8)
    return 0, solution

def ins6(regs, operant, solution):
    numerator = regs[0]
    combo_operant = get_combo_operant(regs, operant)
    denominator = 2 ** combo_operant
    regs[1] = numerator // denominator
    return 0, solution

def ins7(regs, operant, solution):
    numerator = regs[0]
    combo_operant = get_combo_operant(regs, operant)
    denominator = 2 ** combo_operant
    regs[2] = numerator // denominator
    return 0, solution

def get_combo_operant(regs, operant):
    if operant < 0 or operant > 6:
        print("Error in get_combo_operant")
    elif operant < 4:
        combo_operant = operant
    else:
        combo_operant = regs[operant - 4]
    return combo_operant

if __name__ == "__main__":
    main()