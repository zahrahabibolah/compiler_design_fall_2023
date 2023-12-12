# Grammar Description

This grammar defines a simple mathematical expression language. It can be used to parse and evaluate mathematical expressions involving basic arithmetic operations, functions, variables, and constants.

## Language Features

- Supports basic arithmetic operations: addition, subtraction, multiplication, division.
- Handles exponentiation with the `^` operator.
- Recognizes mathematical functions such as cosine (`cos`), sine (`sin`), tangent (`tan`), etc.
- Allows the use of scientific notation for numbers.
- Supports parentheses for grouping expressions.
- Recognizes variables and constants, including `pi`, `e` (Euler's number), and the imaginary unit `i`.

## Grammar Rules

The grammar is defined using Antlr4 syntax and consists of the following main rules:

- `equation`: Represents a mathematical equation composed of two expressions and a relational operator.
- `expression`: Represents a mathematical expression involving addition and subtraction.
- `multiplyingExpression`: Represents a mathematical expression involving multiplication and division.
- `powExpression`: Represents an expression involving exponentiation.
- `signedAtom`: Represents an atom (basic unit) with an optional positive or negative sign.
- `atom`: Represents the basic building blocks of expressions, including scientific numbers, variables, constants, and grouped expressions.

## Mathematical Functions

The grammar includes support for various mathematical functions such as cosine, sine, tangent, logarithms, square root, etc.

## Usage Example

```antlr
equation : expression relop expression EOF;

expression : multiplyingExpression ((PLUS | MINUS) multiplyingExpression)*;

multiplyingExpression : powExpression ((TIMES | DIV) powExpression)*;

powExpression : signedAtom (POW signedAtom)*;

signedAtom : PLUS signedAtom
           | MINUS signedAtom
           | func_
           | atom;

// ... (other rules)

// Mathematical functions
func_ : funcname LPAREN expression (COMMA expression)* RPAREN;

// ... (other rules)

// Function names
funcname : COS | TAN | SIN | ACOS | ATAN | ASIN | LOG | LN | SQRT;
```

 

### Input Example:

```plaintext
result = sqrt(a^2 + b^2) * cos(theta) + 2 * log(e^3) - sin(pi/4)
```

### Expected Output:

**Parse Tree Representation:**

The parser would generate a parse tree for the given input. Here's a simplified textual representation of the parse tree:

```
equation
|-- variable: result
|-- =
|-- expression
|   |-- multiplyingExpression
|       |-- powExpression
|           |-- func_: sqrt
|               |-- expression
|                   |-- expression
|                   |   |-- variable: a
|                   |-- +
|                   |-- expression
|                       |-- variable: b
|       |-- *
|       |-- func_: cos
|           |-- expression
|               |-- variable: theta
|-- +
|-- expression
|   |-- multiplyingExpression
|       |-- NUMBER: 2
|       |-- *
|       |-- func_: log
|           |-- expression
|               |-- powExpression
|                   |-- variable: e
|                   |-- NUMBER: 3
|-- -
|-- func_: sin
|   |-- expression
|       |-- /
|           |-- variable: pi
|           |-- NUMBER: 4
```

**Evaluation:**

Assuming you want to evaluate the expression with specific values for variables `a`, `b`, `theta`, and using known constants like `pi` and `e`, the output might look like:

```plaintext
Result: 3.141592653589793
```

In this example, the expression involves the square root of the sum of squares, cosine, logarithm, and sine functions, as well as constants like `pi` and `e`.



## License

This grammar is provided under the [MIT License](LICENSE) specified in the repository.
