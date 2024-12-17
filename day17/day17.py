def main():
    progs = (2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0)
    progs_string = ',' + ",".join(map(str, progs))
    len_progs_string = len(progs_string.lstrip(','))
    func = [ins0, ins1, ins2, ins3, ins4, ins5, ins6, ins7]
    a_init = 37293246

    while True:
        prog = 0
        solution_parts = []
        regs = [a_init,0,0]
        while prog < len(progs):

            opcode = progs[prog]
            operant = progs[prog+1]

            res = func[opcode](regs, operant, solution_parts)
            if res:
                prog = operant - 2
            prog += 2

        solution = ",".join(solution_parts)

        if a_init == 37293246:
            print(f"Solution for Part 1: {solution}")
            print("Calculating solution for Part 2, this may take a couple of minutes...")
            a_init = 1
        elif len_progs_string > len(solution) + 2:
            a_init *=10
        elif len_progs_string != len(solution):
            a_init = int(a_init * 1.1)
        elif solution[-6:] != progs_string[-6:]:
            a_init += 100000000
        elif solution[-12:] != progs_string[-12:]:
            a_init += 100000
        elif solution[-18:] != progs_string[-18:]:
            a_init += 10000
        elif solution[-20:] != progs_string[-20:]:
            a_init += 10
        else:
            a_init += 1

        if solution == progs_string.lstrip(','):
            print(f"Solution for Part 2: {a_init - 1}")
            break

def ins0(regs, operant, solution):
    numerator = regs[0]
    combo_operant = get_combo_operant(regs, operant)
    denominator = 1 << combo_operant
    regs[0] = numerator // denominator
    return 0

def ins1(regs, operant, solution):
    regs[1] ^= operant
    return 0

def ins2(regs, operant, solution):
    combo_operant = get_combo_operant(regs, operant)
    regs[1] = combo_operant % 8
    return 0

def ins3(regs, operant, solution):
    if regs[0] != 0:
        return 1, solution
    return 0

def ins4(regs, operant, solution):
    regs[1] ^= regs[2]
    return 0

def ins5(regs, operant, solution):
    combo_operant = get_combo_operant(regs, operant)
    solution.append(str(combo_operant % 8))
    return 0

def ins6(regs, operant, solution):
    numerator = regs[0]
    combo_operant = get_combo_operant(regs, operant)
    denominator = 1 << combo_operant
    regs[1] = numerator // denominator
    return 0

def ins7(regs, operant, solution):
    numerator = regs[0]
    combo_operant = get_combo_operant(regs, operant)
    # denominator = 2 ** combo_operant
    denominator = 1 << combo_operant
    regs[2] = numerator // denominator
    return 0

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