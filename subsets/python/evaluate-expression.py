def diff_ways_to_evaluate_expression(input):
    result = []

    for i in range(1, len(input)):
        if not input[i].isdigit() and input[i - 1].isdigit():
            left = diff_ways_to_evaluate_expression(input[:i])
            operator = input[i]
            right = diff_ways_to_evaluate_expression(input[(i + 1):])
            for part_a in left:
                for part_b in right:
                    result.append(eval(f"{part_a}{operator}{part_b}"))

    if not result:
        result.append(input)

    return result


if __name__ == '__main__':
    print(f"Expression evaluations: {diff_ways_to_evaluate_expression('1+2*3')}")
    print(f"Expression evaluations: {diff_ways_to_evaluate_expression('2*3-4-5')}")
