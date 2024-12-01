from collections import Counter

input_lines = open('input1.txt', 'r').readlines()

left_location_list = [int(line[:5]) for line in input_lines]
right_location_list = [int(line.rstrip('\n')[-5:]) for line in input_lines]

def total_distance(left_list, right_list):
    return sum(abs(li-ri) for li, ri in zip(sorted(left_list), sorted(right_list)))

def similarity_score(left_list, right_list):
    right_count = Counter(right_list)
    return sum(li*right_count[li] for li in left_list)

print(total_distance(left_location_list, right_location_list))      # part one
print(similarity_score(left_location_list, right_location_list))    # part two