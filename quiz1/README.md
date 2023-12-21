
```markdown
# Palindrome Recognition with ANTLR4 and Python

This project demonstrates how to use ANTLR4 with Python to recognize palindromes in a given text. The grammar is designed to recognize both string and numeric palindromes.

## Grammar

The grammar defines a palindrome as either a string palindrome or a numeric palindrome. The `palindrome` rule expects the entire input to be a palindrome.

```antlr
grammar palindrome;

start: PALINDROME* EOF;

palindrome: 'z' entry EOF;

entry: 'a' entry 'a'
     | 'b' entry 'b'
     | DIGIT entry DIGIT
     | 'a'
     | 'b'
     | DIGIT
     | ;

DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;
```

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install ANTLR4:**

    Follow the ANTLR4 installation guide: [ANTLR4 Installation Guide](https://github.com/antlr/antlr4/blob/main/doc/getting-started.md)

3. **Generate Lexer and Parser:**

    ```bash
    antlr4 -Dlanguage=Python3 palindrome.g4
    ```

4. **Run the Python Script:**

    ```bash
    python FindPalindromes.py
    ```

5. **Enter Your Input Text When Prompted.**

## Example
![1](https://github.com/zahrahabibolah/compiler_design_fall_2023/blob/main/quiz1/quiz.png?raw=true)


This example demonstrates recognizing and printing both string and numeric palindromes in the provided input text.

## License

This grammar is provided under the [MIT License](LICENSE) specified in the repository.
```
