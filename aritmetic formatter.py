def arithmetic_formatter(problems, show_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    formatted_problems = []
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        try:
            operand1 = int(operand1)
            operand2 = int(operand2)
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

        if operator not in ['+', '-']:
            return "Error: Invalid operator. Please use only '+' or '-'."

        if len(str(operand1)) > 4 or len(str(operand2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(str(operand1)), len(str(operand2))) + 2
        formatted_problem = "{:>{}}\n{}{:>{}}\n{}".format(operand1, max_length, operator, operand2, max_length - 1, '-' * max_length)
        formatted_problems.append(formatted_problem)

    if show_result:
        results = []
        for problem in problems:
            operand1, operator, operand2 = problem.split()
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            results.append(result)

        formatted_results = "    ".join(map(str, results))
        return "\n".join(formatted_problems) + "\n" + formatted_results
    else:
        return "\n".join(formatted_problems)


# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "12 - 38"]
formatted_output = arithmetic_formatter(problems, show_result=True)
print(formatted_output)
