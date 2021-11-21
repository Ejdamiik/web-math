from typing import Dict

PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": -1, ")": 0}

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b,
}


def get_postfix(infix: str) -> str:

    curr_ops = []
    result = ""

    for char in infix:

        if char in PRIORITY:

            if char == "(":
                curr_ops.append(char)
            else:
                while curr_ops != [] and (
                    PRIORITY[curr_ops[-1]] >= PRIORITY[char] and char != "^"
                ):

                    result += " " + curr_ops.pop()

                if char == ')':
                    curr_ops.pop()
                else:
                    curr_ops.append(char)
        else:
            result += char

    while curr_ops != []:
        result += " " + curr_ops.pop()

    return result


def eval_rpn(formula: str, variables: Dict[str, int]) -> int:

    rpn = get_postfix(formula)
    stack = []

    for part in rpn.split(" "):

        if part in OPERATORS:

            b = stack.pop()
            a = stack.pop()

            res = OPERATORS[part](a, b)
            stack.append(res)

        elif part.isdecimal():
            stack.append(int(part))

        elif part.isalpha():
            stack.append(variables[part])


    return stack[-1]
