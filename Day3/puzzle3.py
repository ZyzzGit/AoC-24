corrupted_memory = open("input3.txt", 'r').read()

def extract_int_tuple(string):
    a, b = string.split(',')
    return (int(a), int(b))

def get_mul_tuples(corrupted_memory, always_enabled=True):
    mul_is_enabled = True
    mul_tuples = []
    i = 0
    while i < len(corrupted_memory):
        if corrupted_memory[i-4:i] == 'do()':
            mul_is_enabled = True
        elif corrupted_memory[i-7:i] == "don't()":
            mul_is_enabled = False
        elif corrupted_memory[i-4:i] == 'mul(' and (always_enabled or mul_is_enabled):
            j = i+1
            while j < len(corrupted_memory):
                c = corrupted_memory[j]
                if c == ')':
                    mul_tuples.append(extract_int_tuple(corrupted_memory[i:j]))
                    break
                elif not (c.isdigit() or c == ','): # check if character is valid
                    break
                j += 1
            i = j   # avoid rechecking characters already processed
        i += 1

    return mul_tuples

print(sum(map(lambda tuple: tuple[0] * tuple[1], get_mul_tuples(corrupted_memory))))
print(sum(map(lambda tuple: tuple[0] * tuple[1], get_mul_tuples(corrupted_memory, always_enabled=False))))