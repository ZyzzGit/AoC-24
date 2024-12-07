input_lines = open('input7.txt', 'r').readlines()
equations = [list(map(lambda x: int(x) if x.isnumeric() else int(x[:-1]), line.split())) for line in input_lines]

def equation_holds(equation, concat_enabled):
    lhs = equation[0]
    operands = equation[1:]
    if len(operands) == 1:
        return lhs == operands[0] 
    # "Speed, I am speed": process equation rhs backwards; recursively trying the possible operations
    x = operands[-1]
    lhs_is_divisible = lhs % x == 0
    concat_alt = False
    if concat_enabled:
        lhs_cut = str(lhs)[:-len(str(x))]   # the part before concatenation
        lhs_match = str(lhs)[-len(str(x)):] # the (possibly) concatenated part
        concat_is_possible = lhs_match == str(x) and lhs_cut != ''
        concat_alt = equation_holds([int(lhs_cut)] + operands[:-1], concat_enabled) if concat_is_possible else False
    division_alt = equation_holds([lhs // x] + operands[:-1], concat_enabled) if lhs_is_divisible else False
    subtraction_alt = equation_holds([lhs - x] + operands[:-1], concat_enabled) # subtraction always possible
    return concat_alt or division_alt or subtraction_alt

print(sum([eq[0] for eq in equations if equation_holds(eq, concat_enabled=False)])) # part one
print(sum([eq[0] for eq in equations if equation_holds(eq, concat_enabled=True)]))  # part two
