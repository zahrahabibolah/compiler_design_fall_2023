# Generated from C:/Users/black/compiler_design_fall_2023/HW4/Password.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,22,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,0,0,2,0,2,0,0,23,0,4,1,0,0,0,
        2,19,1,0,0,0,4,5,5,1,0,0,5,6,3,2,1,0,6,7,5,0,0,1,7,1,1,0,0,0,8,9,
        5,2,0,0,9,10,3,2,1,0,10,11,5,2,0,0,11,20,1,0,0,0,12,13,5,3,0,0,13,
        14,3,2,1,0,14,15,5,3,0,0,15,20,1,0,0,0,16,20,5,2,0,0,17,20,5,3,0,
        0,18,20,1,0,0,0,19,8,1,0,0,0,19,12,1,0,0,0,19,16,1,0,0,0,19,17,1,
        0,0,0,19,18,1,0,0,0,20,3,1,0,0,0,1,19
    ]

class PasswordParser ( Parser ):

    grammarFileName = "Password.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'z'", "'a'", "'b'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS" ]

    RULE_palindrome = 0
    RULE_entry = 1

    ruleNames =  [ "palindrome", "entry" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PalindromeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entry(self):
            return self.getTypedRuleContext(PasswordParser.EntryContext,0)


        def EOF(self):
            return self.getToken(PasswordParser.EOF, 0)

        def getRuleIndex(self):
            return PasswordParser.RULE_palindrome

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPalindrome" ):
                listener.enterPalindrome(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPalindrome" ):
                listener.exitPalindrome(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPalindrome" ):
                return visitor.visitPalindrome(self)
            else:
                return visitor.visitChildren(self)




    def palindrome(self):

        localctx = PasswordParser.PalindromeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_palindrome)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(PasswordParser.T__0)
            self.state = 5
            self.entry()
            self.state = 6
            self.match(PasswordParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entry(self):
            return self.getTypedRuleContext(PasswordParser.EntryContext,0)


        def getRuleIndex(self):
            return PasswordParser.RULE_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry" ):
                listener.enterEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry" ):
                listener.exitEntry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry" ):
                return visitor.visitEntry(self)
            else:
                return visitor.visitChildren(self)




    def entry(self):

        localctx = PasswordParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entry)
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(PasswordParser.T__1)
                self.state = 9
                self.entry()
                self.state = 10
                self.match(PasswordParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(PasswordParser.T__2)
                self.state = 13
                self.entry()
                self.state = 14
                self.match(PasswordParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(PasswordParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.match(PasswordParser.T__2)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





