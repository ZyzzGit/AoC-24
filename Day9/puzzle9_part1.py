disk_map = list(open('input9.txt', 'r').read())
disk_map = [int(x) for x in disk_map]

def to_filesystem(disk_map):
    filesystem = []
    for i, k in enumerate(disk_map):
        if i % 2 == 0:  # all even positions in map correspond to files
            filesystem = filesystem + [i//2]*k  
        else:           # odd correspond to spaces
            filesystem = filesystem + ['.']*k
    return filesystem

def compact(filesystem):
    space_indices = [i for i, x in enumerate(filesystem) if x == '.']
    file_indices = [i for i, x in enumerate(filesystem) if x != '.']
    for f in reversed(file_indices):
        if f < min(space_indices):
            break
        filesystem[space_indices.pop(0)] = filesystem[f]
        filesystem[f] = '.'
    return filesystem

def checksum(filesystem):
    i = 0
    checksum = 0
    while filesystem[i] != '.':
        checksum += i * filesystem[i]
        i += 1
    return checksum

print(checksum(compact(to_filesystem(disk_map))))   # part one