# ANTLR Grammar: main

This ANTLR grammar, named `main`, defines rules for parsing and recognizing specific patterns such as national numbers, email addresses, postal codes, decimal numbers, software versions, and website addresses.

## Rules

### `nationalNumber`
- Rule for matching a 10-digit national number.

### `email`
- Rule for matching an email address.

### `postalCode`
- Rule for matching a postal code with specific constraints.

### `decimalNumber`
- Rule for matching a decimal number.

### `softwareVersion`
- Rule for matching a software version number.

### `websiteAddress`
- Rule for matching a website address with a specific format.

## Lexer Rules

- `DIGIT`: Defines a digit.
- `WS`: Skips whitespaces.

## Fragments

- `LOCAL_SUBPART`: Fragment for the local part of an email address.
- `DOMAIN_SUBPART`: Fragment for the domain part of an email address.
- `SUBPART1` and `SUBPART2`: Fragments for parts of a website address.

## Examples

- `5560794651` matches a national number.
- `zahra@gmail.com` matches an email address.
- `3316938845` matches a postal code.
- `2.1` matches a decimal number.
- `2.12.3` matches a software version.
- `http://askskdjiodsfj.com` matches a website address.

## Real input/output

![main](https://github.com/zahrahabibolah/compiler_design_fall_2023/blob/main/HW3/hw3.png?raw=true)


![parse tree](https://github.com/zahrahabibolah/compiler_design_fall_2023/blob/main/HW3/hw3'.png?raw=true)





## Usage

1. **Install ANTLR:** Follow the instructions on the [ANTLR website](https://www.antlr.org/) to install ANTLR.
2. **Generate Lexer and Parser:** Use ANTLR to generate lexer and parser classes for your grammar.
   ```bash
   antlr4 main.g4


## License

This grammar is provided under the [MIT License](LICENSE) specified in the repository.
