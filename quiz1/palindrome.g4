grammar palindrome;

palindrome: 'z' entry EOF;

entry: DIGIT entry DIGIT
     | DIGIT;

DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;
