from z3 import Real, Solver

def solve_part2(hailstones):
    solver = Solver()
    
    rx = Real('rx')
    ry = Real('ry')
    rz = Real('rz')
    vrx = Real('vrx')
    vry = Real('vry')
    vrz = Real('vrz')
    
    for i, (px, py, pz, vx, vy, vz) in enumerate(hailstones):
        t = Real(f't_{i}')
        
        solver.add(rx + vrx * t == px + vx * t)
        solver.add(ry + vry * t == py + vy * t)
        solver.add(rz + vrz * t == pz + vz * t)
        
        solver.add(t >= 0)
    
    if solver.check().r == 1:
        model = solver.model()
        rock_x = model[rx].as_long()
        rock_y = model[ry].as_long()
        rock_z = model[rz].as_long()
        return rock_x + rock_y + rock_z
    return None

def main():
    hailstones = []
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        for line in file:
            pos, vel = line.strip().split('@')
            px, py, pz = map(int, pos.split(','))
            vx, vy, vz = map(int, vel.split(','))
            hailstones.append((px, py, pz, vx, vy, vz))
    
    result = solve_part2(hailstones)
    print(f"Solution for Part 2: {result}")

if __name__ == "__main__":
    main()