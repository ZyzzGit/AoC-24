disk_map = list(open('input9.txt', 'r').read())
disk_map = [int(x) for x in disk_map]

def to_filesystem(disk_map):
    files = []
    spaces = []
    disk_index = 0
    for i, k in enumerate(disk_map):
        disk_range = (disk_index, disk_index + k)
        if i % 2 == 0:  # all even positions in map correspond to files
            file_ID = i//2
            files.append((file_ID, disk_range))
        elif k > 0:     # odd correspond to spaces, and we only keep positive (existing) ones
            spaces.append(disk_range)
        disk_index += k
    return (files, spaces)

def compact(filesystem):
    files, spaces = filesystem
    for i in reversed(range(len(files))):
        file, disk_range = files[i]
        file_start, file_end = disk_range
        for j in range(len(spaces)):
            space_start, space_end = spaces[j]
            if file_end < space_start:
                break
            required_space = file_end - file_start
            space = space_end  - space_start
            if space >= required_space:
                new_file_start = space_start
                new_file_end = space_start + (file_end - file_start)
                files[i] = (file, (new_file_start, new_file_end))
                spaces[j] = (new_file_end, space_end)
                break
    return files

def checksum(files):
    checksum = 0
    for file_ID, disk_range in files:
        start_index, end_index = disk_range
        checksum += sum([file_ID * index for index in range(start_index, end_index)])
    return checksum

print(checksum(compact(to_filesystem(disk_map))))   # part two