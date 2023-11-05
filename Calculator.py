import sys

expression = ""
index = 0



# Represents a node in a binary tree used to build the parse tree for the mathematical expression with each node has a value (an operator or operand) and left and right children (subtrees).
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



# Displays an error message and exit the program with an error code, calls when there is an issue with the input expression.
def error(message):
    sys.stderr.write(f"Error: {message}\n")
    sys.exit(1)



# Compares the current character in the input expression to an expected_token and advances the index to the next character if matches
def match(expected_token):
    global index
    while index < len(expression) and expression[index].isspace():
        index += 1

    if index < len(expression) and expression[index] == expected_token:
        index += 1
    else:
        error(f"Expected '{expected_token}'")



# Skips any white spaces in the input expression by advancing the index until a non-whitespace character is found.
def skip_whitespace():
    global index
    while index < len(expression) and expression[index].isspace():
        index += 1



# Parses and builds the parse tree for the entire mathematical expression, which may consist of one or more terms separated by addition or subtraction operators.
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



# Parses and builds the parse tree for a term, which may consist of one or more factors separated by multiplication, division, or modulo operators.
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



# Parses and builds the parse tree for a factor, which can be a number, a negative number, or an expression enclosed in parentheses. It handles different cases, including recognizing negative numbers and handling parentheses.
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
        while index < len(expression) and (expression[index].isdigit() or expression[index] == " " or expression[index] == "."):
            if expression[index] != " ":
                value += expression[index]
            index += 1
        temp = TreeNode(value)
    else:
        error("Invalid expression")

    return temp



# Displays the parse tree in a human-readable format, with each node and its children indented to indicate the tree structure recursively.
def display_parse_tree(node, level = 0):
    if node is not None:
        display_parse_tree(node.right, level + 1)
        print(" " * 4 * level + node.value)
        display_parse_tree(node.left, level + 1)



# Recursively evaluates the parse tree to calculate the result of the mathematical expression. It performs the arithmetic operations based on the operator in each node and returns the final result.
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
    if node.value.isdigit() or node.value.replace('.', '').isdigit():
        return float(node.value)
    return float(node.value)



# Prompts user to input a mathematical expression. The expr() function is called to parse and build the parse tree, and the resulting parse tree is displayed. Then, the calculate() function is called to evaluate the expression and print the result.
if __name__ == "__main__":
    expression = input("Enter the calculation string, e.g. '34 + 45 * 4 % 7': ")
    index = 0

    parse_tree = expr()

    skip_whitespace()

    if index == len(expression) or (index == len(expression) - 1 and expression[index] == " "):
        print("Parse Tree:")
        display_parse_tree(parse_tree)
        result = calculate(parse_tree)
        print(f"Result = {result}")
    else:
        error("Invalid expression")
