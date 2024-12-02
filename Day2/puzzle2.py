input_lines = open('input2.txt', 'r').readlines()

reports = [list(map(int, line.split())) for line in input_lines]

def is_safe(report):
    difference = [x2-x1 for x1, x2 in zip(report[:-1], report[1:])]
    all_same_direction = all(d > 0 for d in difference) or all(d < 0 for d in difference)   # all levels increasing or all decreasing
    safe_difference = all(1 <= abs(d) and abs(d) <= 3 for d in difference)  # adjacant levels differ with 1 <= d <= 3
    return all_same_direction and safe_difference

def is_safe_1off_tolerance(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True

print(sum(1 for report in reports if is_safe(report)))                  # part one
print(sum(1 for report in reports if is_safe_1off_tolerance(report)))   # part two