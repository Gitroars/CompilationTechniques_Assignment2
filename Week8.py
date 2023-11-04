import sys
import math
import re

expression = ""
tokens = []


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def error(message):
    sys.stderr.write(f"Error: {message}\n")
    sys.exit(1)


def tokenize(expression):
    # Define regular expressions for numbers, operators, and parentheses
    regex = r"(\d+|\+|-|\*|/|%|\(|\))"
    tokens = re.findall(regex, expression)
    # Remove whitespace from the list of tokens
    tokens = [token for token in tokens if not token.isspace()]
    return tokens


def expr():
    temp = term()

    while tokens and (tokens[0] in "+-"):
        op = tokens.pop(0)
        right = term()
        temp = TreeNode(op, temp, right)

    return temp


def term():
    temp = factor()

    while tokens and (tokens[0] in "*/%"):
        op = tokens.pop(0)
        right = factor()
        temp = TreeNode(op, temp, right)

    return temp


def factor():
    token = tokens.pop(0)

    if token == "(":
        temp = expr()
        if tokens.pop(0) != ")":
            error("Expected closing parenthesis")
    elif token.isdigit() or (
        token == "-" and (not tokens or tokens[0] in "0123456789")
    ):
        temp = TreeNode(token)
    else:
        error("Invalid expression")

    return temp


def display_parse_tree(node, level=0):
    if node is not None:
        display_parse_tree(node.right, level + 1)
        print(" " * 4 * level + node.value)
        display_parse_tree(node.left, level + 1)


def calculate(node):
    if node.left is None and node.right is None:
        return int(node.value)
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


if __name__ == "__main__":
    expression = input("Enter the calculation string, e.g. '34 + 45 * 4 % 7': ")
    tokens = tokenize(expression)
    parse_tree = expr()

    if not tokens:
        print("Parse Tree:")
        display_parse_tree(parse_tree)
        result = calculate(parse_tree)
        print(f"Result = {result}")
    else:
        error("Invalid expression")
