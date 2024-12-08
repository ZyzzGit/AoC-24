input_lines = open('input8.txt', 'r').readlines()
antenna_map = [list(line.strip()) for line in input_lines]

def out_of_bounds(pos, matrix):
    i, j = pos
    height = len(matrix)
    width = len(matrix[0])
    return i < 0 or i >= height or j < 0 or j >= width

def get_harmonic_antinodes(antenna1_pos, antenna2_pos, matrix):   # for part two only
    new_antinodes = []
    i, j = antenna1_pos
    k, l = antenna2_pos
    antinode = (i, j)
    m = 2   
    while not out_of_bounds (antinode, matrix): # corresponding to antenna1
        new_antinodes.append(antinode)
        antinode = (m*i-(m-1)*k, m*j-(m-1)*l)
        m += 1
    antinode = (k, l)
    m = 2
    while not out_of_bounds (antinode, matrix): # corresponding to antenna2
        new_antinodes.append(antinode)
        antinode = (m*k-(m-1)*i, m*l-(m-1)*j)
        m += 1
    return new_antinodes

def get_antinodes(matrix, resonant_harmonics=False):
    antennas = {}   # antennas[x] contains a set with the locations of all x-frequency antennas
    antinodes = set()
    for i in range(len(matrix)):
        for j, x in enumerate(matrix[i]):
            if x != '.':
                if x not in antennas:
                    antennas[x] = set()
                for (k, l) in antennas[x]:  # compute new antinodes wrt the other antennas
                    if resonant_harmonics:
                        new_antinodes = get_harmonic_antinodes((i, j), (k, l), matrix)
                    else:
                        antinode1 = (2*i-k, 2*j-l)
                        antinode2 = (2*k-i, 2*l-j)
                        new_antinodes = [antinode1, antinode2]
                    for antinode in new_antinodes:
                        if not out_of_bounds(antinode, matrix):
                            antinodes.add(antinode)
                antennas[x].add((i, j)) 
    return antinodes

print(len(get_antinodes(antenna_map)))                          # part one
print(len(get_antinodes(antenna_map, resonant_harmonics=True))) # part two