# Generated from C:/Users/black/compiler_design_fall_2023/HW4/HW3/main.g4 by ANTLR 4.13.1
from antlr4 import *
import re
from antlr4 import FileStream
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,126,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,27,8,0,
        11,0,12,0,28,1,1,4,1,32,8,1,11,1,12,1,33,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,4,5,69,8,5,11,5,12,5,
        70,1,5,1,5,4,5,75,8,5,11,5,12,5,76,1,6,4,6,80,8,6,11,6,12,6,81,1,
        6,1,6,4,6,86,8,6,11,6,12,6,87,1,6,1,6,4,6,92,8,6,11,6,12,6,93,1,
        7,4,7,97,8,7,11,7,12,7,98,1,8,4,8,102,8,8,11,8,12,8,103,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,4,9,114,8,9,11,9,12,9,115,1,10,1,10,1,11,
        4,11,121,8,11,11,11,12,11,122,1,11,1,11,0,0,12,1,0,3,0,5,1,7,2,9,
        3,11,4,13,5,15,0,17,0,19,6,21,7,23,8,1,0,4,7,0,37,37,43,43,45,46,
        48,57,65,90,95,95,97,122,4,0,45,46,48,57,65,90,97,122,1,0,48,57,
        3,0,9,10,13,13,32,32,132,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,26,
        1,0,0,0,3,31,1,0,0,0,5,35,1,0,0,0,7,41,1,0,0,0,9,52,1,0,0,0,11,68,
        1,0,0,0,13,79,1,0,0,0,15,96,1,0,0,0,17,101,1,0,0,0,19,105,1,0,0,
        0,21,117,1,0,0,0,23,120,1,0,0,0,25,27,7,0,0,0,26,25,1,0,0,0,27,28,
        1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,2,1,0,0,0,30,32,7,1,0,0,31,
        30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,4,1,0,0,
        0,35,36,3,1,0,0,36,37,5,64,0,0,37,38,3,3,1,0,38,39,5,46,0,0,39,40,
        3,3,1,0,40,6,1,0,0,0,41,42,3,21,10,0,42,43,3,21,10,0,43,44,3,21,
        10,0,44,45,3,21,10,0,45,46,3,21,10,0,46,47,3,21,10,0,47,48,3,21,
        10,0,48,49,3,21,10,0,49,50,3,21,10,0,50,51,3,21,10,0,51,8,1,0,0,
        0,52,53,5,49,0,0,53,54,2,51,57,0,54,55,1,0,0,0,55,56,3,21,10,0,56,
        57,6,4,0,0,57,58,3,21,10,0,58,59,3,21,10,0,59,60,3,21,10,0,60,61,
        3,21,10,0,61,62,3,21,10,0,62,63,3,21,10,0,63,64,3,21,10,0,64,65,
        3,21,10,0,65,66,3,21,10,0,66,10,1,0,0,0,67,69,7,2,0,0,68,67,1,0,
        0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,74,
        5,46,0,0,73,75,7,2,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,
        76,77,1,0,0,0,77,12,1,0,0,0,78,80,7,2,0,0,79,78,1,0,0,0,80,81,1,
        0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,85,5,46,0,0,84,
        86,7,2,0,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,
        0,88,89,1,0,0,0,89,91,5,46,0,0,90,92,7,2,0,0,91,90,1,0,0,0,92,93,
        1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,14,1,0,0,0,95,97,7,0,0,0,
        96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,16,1,
        0,0,0,100,102,7,1,0,0,101,100,1,0,0,0,102,103,1,0,0,0,103,101,1,
        0,0,0,103,104,1,0,0,0,104,18,1,0,0,0,105,106,3,15,7,0,106,107,5,
        58,0,0,107,108,5,47,0,0,108,109,5,47,0,0,109,110,1,0,0,0,110,113,
        3,15,7,0,111,112,5,46,0,0,112,114,3,17,8,0,113,111,1,0,0,0,114,115,
        1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,20,1,0,0,0,117,118,7,
        2,0,0,118,22,1,0,0,0,119,121,7,3,0,0,120,119,1,0,0,0,121,122,1,0,
        0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,6,11,
        1,0,125,24,1,0,0,0,12,0,28,33,70,76,81,87,93,98,103,115,122,2,1,
        4,0,6,0,0
    ]

class mainLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EMAIL = 1
    NATIONAL_NUMBER = 2
    POSTAL_CODE = 3
    DECIMAL_NUMBER = 4
    SOFTWARE_VERSION = 5
    WEBSITE_ADDRESS = 6
    DIGIT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "EMAIL", "NATIONAL_NUMBER", "POSTAL_CODE", "DECIMAL_NUMBER", 
            "SOFTWARE_VERSION", "WEBSITE_ADDRESS", "DIGIT", "WS" ]

    ruleNames = [ "LOCAL_SUBPART", "DOMAIN_SUBPART", "EMAIL", "NATIONAL_NUMBER", 
                  "POSTAL_CODE", "DECIMAL_NUMBER", "SOFTWARE_VERSION", "SUBPART1", 
                  "SUBPART2", "WEBSITE_ADDRESS", "DIGIT", "WS" ]

    grammarFileName = "main.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.POSTAL_CODE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def POSTAL_CODE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            input.LT(1).getText() != "0" and input.LT(1).getText() != "2"



            input_file = "test.txt"
            input_stream = FileStream(input_file)
            lexer = mainLexer(input_stream)
            def custom_check_national_code(input_file):
                # Extract sequences of 10 digits
                national_code_pattern = re.compile(r'\b\d{10}\b')
                national_codes = national_code_pattern.findall(input_file)

                for code in national_codes:
                    if not re.match(r'^[0-9]{10}$', input_file):
                        return False
                    else:
                        for i in range(10):
                            if re.match(r'^' + str(i) + r'{10}$', input_file):
                                return False
                            else:
                                sum_value = sum((10 - i) * int(input_file[i]) for i in range(9))
                                ret = sum_value % 11
                                parity = int(input_file[9])
                    if (ret < 2 and ret == parity) or (ret >= 2 and ret == 11 - parity):
                        return True

                return False
            if custom_check_national_code(input_file) is False:
                localctx = 3
     


