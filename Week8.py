import sys

expression = ""
index = 0


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def error(message):
    sys.stderr.write(f"Error: {message}\n")
    sys.exit(1)


def match(expected_token):
    global index
    while index < len(expression) and expression[index].isspace():
        index += 1

    if index < len(expression) and expression[index] == expected_token:
        index += 1
    else:
        error(f"Expected '{expected_token}'")


def skip_whitespace():
    global index
    while index < len(expression) and expression[index].isspace():
        index += 1


def expr():
    temp = term()

    while index < len(expression) and (expression[index] in "+-"):
        op = expression[index]
        skip_whitespace()
        match(op)
        skip_whitespace()
        right = term()
        temp = TreeNode(op, temp, right)

    return temp


def term():
    temp = factor()

    while index < len(expression) and (expression[index] in "*/%"):
        op = expression[index]
        skip_whitespace()
        match(op)
        skip_whitespace()
        right = factor()
        temp = TreeNode(op, temp, right)

    return temp


def factor():
    global index

    skip_whitespace()

    if index < len(expression) and expression[index] == "(":
        match("(")
        temp = expr()
        match(")")
    elif index < len(expression) and (
        expression[index].isdigit()
        or (
            expression[index] == "-"
            and (index == 0 or (index > 0 and expression[index - 1] in "+-*/%"))
        )
    ):
        value = ""
        while index < len(expression) and (
            expression[index].isdigit() or expression[index] == " "
        ):
            if expression[index] != " ":
                value += expression[index]
            index += 1
        temp = TreeNode(value)
    else:
        error("Invalid expression")

    return temp


def display_parse_tree(node, level=0):
    if node is not None:
        display_parse_tree(node.right, level + 1)
        print(" " * 4 * level + node.value)
        display_parse_tree(node.left, level + 1)


def calculate(node):
    if node.left is not None and node.right is not None:
        left_result = calculate(node.left)
        right_result = calculate(node.right)
        if node.value == "+":
            return left_result + right_result
        elif node.value == "-":
            return left_result - right_result
        elif node.value == "*":
            return left_result * right_result
        elif node.value == "/":
            if right_result == 0:
                error("Division by zero")
            return left_result / right_result
        elif node.value == "%":
            if right_result == 0:
                error("Modulo by zero")
            return left_result % right_result
    if node.value.isdigit():
        return int(node.value)
    return float(node.value)


if __name__ == "__main__":
    expression = input("Enter the calculation string, e.g. '34 + 45 * 4 % 7': ")
    index = 0

    parse_tree = expr()

    skip_whitespace()

    if index == len(expression) or (
        index == len(expression) - 1 and expression[index] == " "
    ):
        print("Parse Tree:")
        display_parse_tree(parse_tree)
        result = calculate(parse_tree)
        print(f"Result = {result}")
    else:
        error("Invalid expression")
