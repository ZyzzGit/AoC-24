input_lines = open('input5.txt', 'r').readlines()

split_index = input_lines.index('\n')
ordering_rules = {} # ordering_rules[k] gives a list of all pages which should be printed after page k
update_orders = [line.strip().split(',') for line in input_lines[split_index+1:]]
update_orders = list(map(lambda list: [int(page) for page in list], update_orders))

for i in range(split_index):
    page1 = int(input_lines[i][0:2])
    page2 = int(input_lines[i][3:5])
    if page1 not in ordering_rules:
        ordering_rules[page1] = []
    ordering_rules[page1].append(page2)

def is_correctly_ordered(update_order):
    for i, page in enumerate(update_order):
        if page not in ordering_rules:
            continue
        for other_page in ordering_rules[page]:
            if other_page in update_order[0:i]:
                return False
    return True

def middle_page_number(update_order):
    return update_order[len(update_order)//2]

def correct(update_order):
    while not is_correctly_ordered(update_order):
        for i, page in enumerate(update_order):
            if page not in ordering_rules:
                continue
            for other_page in ordering_rules[page]:
                for j in range(i):
                    if update_order[j] == other_page:
                        update_order.insert(i+1, update_order.pop(j))   # move misordered item in front of reference page
    return update_order

print(sum(middle_page_number(update_order) for update_order in update_orders if is_correctly_ordered(update_order)))                # part one
print(sum(middle_page_number(correct(update_order)) for update_order in update_orders if not is_correctly_ordered(update_order)))   # part two