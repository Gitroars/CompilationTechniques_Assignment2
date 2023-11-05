# CompilationTechniques_Assignment2

### Assignment By:
- Arvin Yuwono / 2502009721
- Christopher Owen / 2502019180

## Explanation & Discussion
Top-down Parsing

The parser code operates in a top-down direction using recursive descent parsing. The parser starts with the highest-level construct and recursively breaks it down into smaller sub-constructs. In the code, the highest-level construct is the expr() function, which handles the entire mathematical expression. This function calls other functions, such as term() and factor(), to handle lower-level constructs. These lower-level constructs are parsed recursively until the smallest units of the expression are recognized, and a parse tree is constructed.

The sequence of function calls and the structure of the code ensure that the parser first identifies the highest-level operations and expressions (e.g., addition and subtraction), and then it drills down to handle lower-level operations (e.g., multiplication, division, and modulo) and operands (e.g., numbers and negative numbers) within the expression. It is well-suited for handling mathematical expressions, as it mirrors the natural structure of such expressions and ensures that the operator precedence rules are correctly applied.

Depth-first Search

The parser code employs a depth-first search strategy while parsing the input mathematical expression. Depth-first search is a common strategy used in recursive descent parsing, which is the parsing technique used in this code. The parser explores as far down a particular path in the input expression as possible before backtracking when necessary. This strategy ensures that the parser analyzes the input expression from left to right and constructs a parse tree that accurately represents the operator precedence and associativity rules of the mathematical expressions.
