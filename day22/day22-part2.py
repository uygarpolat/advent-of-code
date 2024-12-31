from dataclasses import dataclass
from typing import List, Set, Dict, Tuple, FrozenSet
from collections import defaultdict, deque

@dataclass(frozen=True)
class Block:
    x: FrozenSet[int]
    y: FrozenSet[int]
    z: FrozenSet[int]
    
    @property
    def min_z(self) -> int:
        return min(self.z)
    
    @property
    def max_z(self) -> int:
        return max(self.z)
    
    def fall_one_level(self) -> 'Block':
        return Block(
            self.x,
            self.y,
            frozenset(z - 1 for z in self.z)
        )
    
    @classmethod
    def from_coordinates(cls, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> 'Block':
        return cls(
            frozenset(range(x1, x2 + 1)),
            frozenset(range(y1, y2 + 1)),
            frozenset(range(z1, z2 + 1))
        )

def has_intersection(block1: Block, block2: Block) -> bool:
    return (block1.x & block2.x and 
            block1.y & block2.y and 
            block1.z & block2.z)

def build_support_graph(blocks: List[Block]) -> Tuple[Dict[Block, Set[Block]], Dict[Block, Set[Block]]]:
    supported_by = defaultdict(set)
    supports = defaultdict(set)
    
    sorted_blocks = sorted(blocks, key=lambda b: b.min_z)
    
    for i, upper in enumerate(sorted_blocks):
        if upper.min_z == 1:
            continue
            
        test_block = upper.fall_one_level()
        for lower in sorted_blocks[:i]:
            if lower.max_z == upper.min_z - 1 and has_intersection(test_block, lower):
                supported_by[upper].add(lower)
                supports[lower].add(upper)
    
    return dict(supported_by), dict(supports)

def count_chain_reaction(block: Block, supported_by: Dict[Block, Set[Block]], supports: Dict[Block, Set[Block]]) -> int:
    falling = {block}
    queue = deque([block])
    
    while queue:
        current = queue.popleft()
        for upper in supports.get(current, set()):
            if upper not in falling:
                remaining_supports = supported_by[upper] - falling
                if not remaining_supports:
                    falling.add(upper)
                    queue.append(upper)
    
    return len(falling) - 1

def main():
    blocks: List[Block] = []
    
    with open("input.txt", 'r') as file:
        for line in file:
            start, end = line.strip().split('~')
            x1, y1, z1 = map(int, start.split(','))
            x2, y2, z2 = map(int, end.split(','))
            blocks.append(Block.from_coordinates(x1, y1, z1, x2, y2, z2))
    
    blocks.sort(key=lambda b: b.min_z)
    
    settled_blocks: List[Block] = []
    spatial_index: Dict[int, List[Block]] = defaultdict(list)
    
    for block in blocks:
        current = block
        while current.min_z > 1:
            next_block = current.fall_one_level()
            found_collision = False
            
            relevant_blocks = spatial_index[min(next_block.z)]
            for other_block in relevant_blocks:
                if has_intersection(next_block, other_block):
                    found_collision = True
                    break
            
            if found_collision:
                break
            current = next_block
        
        for z in current.z:
            spatial_index[z].append(current)
        settled_blocks.append(current)
    
    supported_by, supports = build_support_graph(settled_blocks)
    

    total_falling = 0    
    for i, block in enumerate(settled_blocks, 1):
        falling = count_chain_reaction(block, supported_by, supports)
        total_falling += falling
    
    print(f"Solutin for Part 2: {total_falling}")

if __name__ == "__main__":
    main()