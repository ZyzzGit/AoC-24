import operator
import numpy as np

input_lines = open('input6.txt', 'r').readlines()
lab_map = np.array([list(line.strip()) for line in input_lines])

class Guard():
    def __init__(self, start_pos, start_dir):
        self.pos = start_pos
        self.dir = start_dir
        self.left_area = False
        self.has_looped = False
        self.visited_states = set() # each state is a tuple (pos, dir)

    def try_move(self, matrix):
        next_pos = tuple(map(operator.add, self.pos, self.dir))
        if next_pos[0] < 0 or next_pos[0] >= matrix.shape[0] or next_pos[1] < 0 or next_pos[1] >= matrix.shape[1]:
            self.left_area = True
        elif matrix[next_pos] == '#':
            return False
        elif (self.pos, self.dir) in self.visited_states:
            self.has_looped = True
        self.visited_states.add((self.pos, self.dir))
        self.pos = next_pos
        return True
    
    def rotate(self):
        match self.dir:
            case (-1, 0): self.dir = ( 0, 1)
            case ( 0, 1): self.dir = ( 1, 0)
            case ( 1, 0): self.dir = ( 0,-1)
            case ( 0,-1): self.dir = (-1, 0)

start_dir=(-1,0)
start_pos = tuple([int(x) for x in np.where(lab_map == '^')])

def get_visited_positions(matrix, start_pos, start_dir):
    guard = Guard(start_pos, start_dir)
    while not guard.left_area:
        while not guard.try_move(matrix):
            guard.rotate()
    return set([state[0] for state in guard.visited_states])

def count_possible_obstruction_positions(matrix, start_pos, start_dir):
    count = 0
    visited_positions = get_visited_positions(matrix, start_pos, start_dir)
    for pos in visited_positions:
        matrix[pos] = '#'
        guard = Guard(start_pos, start_dir)
        while not (guard.left_area or guard.has_looped):
            while not guard.try_move(matrix):
                guard.rotate()
        if guard.has_looped:
            count += 1
        matrix[pos] = '.'   # restore map for next iteration
    return count

print(len(get_visited_positions(lab_map, start_pos, start_dir)))            # part one
print(count_possible_obstruction_positions(lab_map, start_pos, start_dir))  # part two