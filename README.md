# arthimetic-formatter
import re

def arithmetic_arranger(problems, show_answers=False):

  # Check that number of problems does not exceed 5
  if len(problems) > 5:
    return "Error: Too many problems."

  formatted_problems = ""
  first_row = ""
  second_row = "" 
  lines = ""
  solutions = ""

  for problem in problems:

    # Split each problem into operands and operator
    problem_parts = re.split(' +', problem) 
    left_operand = problem_parts[0]
    operator = problem_parts[1]
    right_operand = problem_parts[2]

    # Check if operands are digits
    if not left_operand.isdigit() or not right_operand.isdigit():
      return "Error: Numbers must only contain digits."

    # Check length of operands
    if len(left_operand) > 4 or len(right_operand) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Get length of longest operand
    length = max(len(left_operand), len(right_operand)) + 2

    # Format first row 
    first_row += left_operand.rjust(length)
    # Format second row
    second_row += operator + right_operand.rjust(length - 1)
    # Format lines 
    lines += "-" * length
    # Get solution 
    if operator == "+":
      solution = str(int(left_operand) + int(right_operand))
    elif operator == "-":
      solution = str(int(left_operand) - int(right_operand))
    else:
      return "Error: Operator must be '+' or '-'."

    # Format solutions row
    solutions += solution.rjust(length) 

    # Add space between problems 
    formatted_problems += first_row.rstrip() + "    " 
    second_row += "    "
    lines += "    "
    solutions += "    "

  # Construct arranged problems 
  arranged_problems = formatted_problems.rstrip() + "\n" + second_row.rstrip() + "\n" + lines.rstrip()

  if show_answers:
    arranged_problems += "\n" + solutions.rstrip()

  return arranged_problems
