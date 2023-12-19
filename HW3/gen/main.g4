grammar main;

start : nationalNumber email postalCode decimalNumber softwareVersion websiteAddress EOF;

//Email
fragment LOCAL_SUBPART : [a-zA-Z0-9._%+-]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9.-]+;
EMAIL: LOCAL_SUBPART '@' DOMAIN_SUBPART '.' DOMAIN_SUBPART;

// National Number
NATIONAL_NUMBER: DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT ;

// Postal Code
POSTAL_CODE : {input.LT(1).getText() != "0" && input.LT(1).getText() != "2" } DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT;

// Decimal Number
DECIMAL_NUMBER: [0-9]+ '.' [0-9]+;

// Software Version
SOFTWARE_VERSION: [0-9]+ '.' [0-9]+ '.' [0-9]+;

// Website Address
fragment SUBPART1 : [a-zA-Z0-9._%+-]+;
fragment SUBPART2 : [a-zA-Z0-9.-]+;
WEBSITE_ADDRESS: SUBPART1 '://' SUBPART1 ('.' SUBPART2)+;

// Rules
nationalNumber: NATIONAL_NUMBER;
email: EMAIL;
postalCode: POSTAL_CODE;
decimalNumber: DECIMAL_NUMBER;
softwareVersion: SOFTWARE_VERSION;
websiteAddress: WEBSITE_ADDRESS;

DIGIT: [0-9];
WS: [ \t\r\n]+ -> skip;


