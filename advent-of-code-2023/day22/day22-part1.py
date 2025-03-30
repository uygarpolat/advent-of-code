from dataclasses import dataclass
from typing import List, Set, Dict, Tuple, FrozenSet
import numpy as np
from collections import defaultdict

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

def get_supported_by(block: Block, blocks: List[Block]) -> Set[Block]:
    supporting = set()
    test_block = block.fall_one_level()
    
    for other in blocks:
        if other != block and has_intersection(test_block, other):
            supporting.add(other)
    
    return supporting

def get_supporting(block: Block, blocks: List[Block]) -> Set[Block]:
    supported = set()
    for other in blocks:
        if other != block and other.min_z == block.max_z + 1:
            test_block = other.fall_one_level()
            if has_intersection(test_block, block):
                supported.add(other)
    return supported

def can_safely_disintegrate(block: Block, blocks: List[Block]) -> bool:
    blocks_above = get_supporting(block, blocks)
    
    for above_block in blocks_above:
        supporting_blocks = get_supported_by(above_block, blocks)
        if len(supporting_blocks) == 1:
            return False
    return True

def main():
    blocks: List[Block] = []
    ground_blocks: List[Block] = []
    
    with open("input.txt", 'r') as file:
        for line in file:
            start, end = line.strip().split('~')
            x1, y1, z1 = map(int, start.split(','))
            x2, y2, z2 = map(int, end.split(','))
            
            block = Block.from_coordinates(x1, y1, z1, x2, y2, z2)
            if z1 == 1:
                ground_blocks.append(block)
            else:
                blocks.append(block)
    
    blocks.sort(key=lambda b: b.min_z)
    
    spatial_index: Dict[int, List[Block]] = defaultdict(list)
    for block in ground_blocks:
        for z in block.z:
            spatial_index[z].append(block)
    
    settled_blocks: List[Block] = []
    
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
    
    settled_blocks.extend(ground_blocks)
    
    safe_count = 0
    total_blocks = len(settled_blocks)
    for i, block in enumerate(settled_blocks):
        if can_safely_disintegrate(block, settled_blocks):
            safe_count += 1
    
    print(f"Solution for Part 1: {safe_count}")

if __name__ == "__main__":
    main()