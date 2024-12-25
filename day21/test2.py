from queue import PriorityQueue
from typing import List, Tuple, Dict
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class State:
    cost: int
    pointers: List[Tuple[int, int]]  # Position on each keypad
    typed: str
    history: List[str]  # Keep track of moves that got us here
    target_index: int   # Track which character in target we're trying to type

    def __lt__(self, other):
        return self.cost < other.cost

class KeypadSolver:
    def __init__(self):
        # Define the three keypads (two directional, one numeric)
        self.pads = [
            [['x', '^', 'A'],
             ['<', 'v', '>']],
            
            [['x', '^', 'A'],
             ['<', 'v', '>']],
            
            [['7', '8', '9'],
             ['4', '5', '6'],
             ['1', '2', '3'],
             ['x', '0', 'A']]
        ]
        
        # Initial positions (A button on each keypad)
        self.initial_pointers = [(0, 2), (0, 2), (3, 2)]
        self.moves = ['<', '>', 'v', '^', 'A']
        
        # Precalculate valid positions for each keypad
        self.valid_positions = self._calculate_valid_positions()

    def _calculate_valid_positions(self) -> List[set]:
        """Precalculate all valid positions for each keypad"""
        valid_pos = []
        for pad_idx, pad in enumerate(self.pads):
            positions = set()
            for i in range(len(pad)):
                for j in range(len(pad[0])):
                    if self.is_valid_position(pad_idx, (i, j)):
                        positions.add((i, j))
            valid_pos.append(positions)
        return valid_pos

    def is_valid_position(self, pad_idx: int, pos: Tuple[int, int]) -> bool:
        """Check if a position is valid on a given keypad"""
        pad = self.pads[pad_idx]
        rows = len(pad)
        cols = len(pad[0])
        
        row, col = pos
        # Special case for gaps
        if rows == 4 and row == 3 and col == 0:  # Numeric keypad
            return False
        if rows == 2 and row == 0 and col == 0:  # Directional keypad
            return False
            
        return 0 <= row < rows and 0 <= col < cols

    def get_char_at(self, pad_idx: int, pos: Tuple[int, int]) -> str:
        """Get character at position on keypad"""
        return self.pads[pad_idx][pos[0]][pos[1]]

    def move_position(self, pos: Tuple[int, int], move: str) -> Tuple[int, int]:
        """Calculate new position after a move"""
        moves_map = {
            '<': (0, -1),
            '>': (0, 1),
            'v': (1, 0),
            '^': (-1, 0)
        }
        if move not in moves_map:
            return pos
            
        delta = moves_map[move]
        return (pos[0] + delta[0], pos[1] + delta[1])

    def find_position_of_char(self, pad_idx: int, target: str) -> Tuple[int, int]:
        """Find position of a character on a keypad"""
        pad = self.pads[pad_idx]
        for i in range(len(pad)):
            for j in range(len(pad[0])):
                if pad[i][j] == target:
                    return (i, j)
        return None

    def solve_code(self, target: str) -> Tuple[int, List[str]]:
        """Find shortest sequence to type the target code"""
        pq = PriorityQueue()
        seen = set()
        
        # Initialize with starting state
        initial_state = State(0, self.initial_pointers.copy(), "", [], 0)
        pq.put(initial_state)
        
        # For debugging
        iterations = 0
        max_iterations = 1000000  # Set a reasonable limit
        
        while not pq.empty() and iterations < max_iterations:
            iterations += 1
            state = pq.get()
            
            # If we've typed the full target, we're done
            if state.typed == target:
                print(f"Solution found in {iterations} iterations")
                return state.cost, state.history
            
            # Optimization: if we've typed more than target length, skip
            if len(state.typed) > len(target):
                continue
                
            # If we've typed something that doesn't match target so far, skip
            if not target.startswith(state.typed):
                continue
            
            # Create state key for detecting cycles
            state_key = (tuple(state.pointers), state.typed)
            if state_key in seen:
                continue
            seen.add(state_key)
            
            # Try each possible move
            for move in self.moves:
                if move == 'A':
                    new_state = self.handle_activation(state, target)
                    if new_state and new_state.typed != state.typed:  # Only add if we actually typed something
                        pq.put(new_state)
                else:
                    new_pos = self.move_position(state.pointers[0], move)
                    if new_pos in self.valid_positions[0]:
                        new_pointers = [new_pos] + state.pointers[1:]
                        new_history = state.history + [move]
                        new_state = State(
                            state.cost + 1,
                            new_pointers,
                            state.typed,
                            new_history,
                            state.target_index
                        )
                        pq.put(new_state)
            
            # Debug print every 10000 iterations
            if iterations % 10000 == 0:
                print(f"Iteration {iterations}, Queue size: {pq.qsize()}, Current typed: {state.typed}")
        
        if iterations >= max_iterations:
            print("Reached maximum iterations!")
        return None  # No solution found

    def handle_activation(self, state: State, target: str) -> State:
        """Handle cascading activation through the keypads"""
        new_state = deepcopy(state)
        new_state.cost += 1
        new_state.history.append('A')
        
        # Get character at current position on first keypad
        char = self.get_char_at(0, state.pointers[0])
        
        if char == 'A':
            # If A, activate next keypad
            char2 = self.get_char_at(1, state.pointers[1])
            if char2 == 'A':
                # If A on second keypad, get character from numeric keypad
                final_char = self.get_char_at(2, state.pointers[2])
                new_state.typed += final_char
                new_state.target_index += 1
            
        return new_state

def main():
    solver = KeypadSolver()
    # Start with just one code for testing
    codes = ["029A"]  # Test with just the first code initially
    total_complexity = 0
    
    for code in codes:
        print(f"\nSolving for code: {code}")
        num_value = int(''.join(filter(str.isdigit, code)))
        result = solver.solve_code(code)
        
        if result:
            moves_count, moves = result
            complexity = moves_count * num_value
            total_complexity += complexity
            print(f"Code: {code}")
            print(f"Moves: {''.join(moves)}")
            print(f"Length: {moves_count}")
            print(f"Complexity: {complexity}\n")
        else:
            print(f"Failed to find solution for {code}")
        
    print(f"Total complexity: {total_complexity}")

if __name__ == "__main__":
    main()