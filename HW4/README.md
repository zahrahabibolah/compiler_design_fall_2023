# ANTLR Grammar: Password

This ANTLR grammar, called "password", defines rules for validating passwords longer than 8 that contain at least one symbol and an uppercase English letter without a space. The password consists of characters (CHAR) and can be followed by an end-of-file (EOF).
## Rules

### `password`
- Rule for defining the password, composed of one or more characters.

### `CHAR`
- Rule for a single character in the password. It can be an uppercase letter, lowercase letter, digit, symbol, or EOF.

### `DIGIT`
- Rule for matching a digit.

### `UPPERCASE`
- Rule for matching an uppercase letter.

### `LOWERCASE`
- Rule for matching a lowercase letter.

### `SYMBOL`
- Rule for matching a symbol from the specified set.

## Lexer Rules

- `WS`: Skips whitespaces.

## Fragments

- `UPPERCASE`, `LOWERCASE`, `DIGIT`, and `SYMBOL`: Fragments defining character classes.

## Examples

- `Password123!` is a valid password.
- `123456789+-*/ D` is an invalid password (missing uppercase letter and digit).
- `SYM@bol` is an invalid password.


## Output/Input
![Alt Text](Image URL)

## Usage

1. **Install ANTLR:** Follow the instructions on the [ANTLR website](https://www.antlr.org/) to install ANTLR.
2. **Generate Lexer and Parser:** Use ANTLR to generate lexer and parser classes for your grammar.
   ```bash
   antlr4 Password.g4
