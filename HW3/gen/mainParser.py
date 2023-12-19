# Generated from C:/Users/black/compiler_design_fall_2023/HW4/HW3/main.g4 by ANTLR 4.13.1
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
        4,1,8,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,27,0,14,1,0,0,0,2,
        22,1,0,0,0,4,24,1,0,0,0,6,26,1,0,0,0,8,28,1,0,0,0,10,30,1,0,0,0,
        12,32,1,0,0,0,14,15,3,2,1,0,15,16,3,4,2,0,16,17,3,6,3,0,17,18,3,
        8,4,0,18,19,3,10,5,0,19,20,3,12,6,0,20,21,5,0,0,1,21,1,1,0,0,0,22,
        23,5,2,0,0,23,3,1,0,0,0,24,25,5,1,0,0,25,5,1,0,0,0,26,27,5,3,0,0,
        27,7,1,0,0,0,28,29,5,4,0,0,29,9,1,0,0,0,30,31,5,5,0,0,31,11,1,0,
        0,0,32,33,5,6,0,0,33,13,1,0,0,0,0
    ]

class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "EMAIL", "NATIONAL_NUMBER", "POSTAL_CODE", 
                      "DECIMAL_NUMBER", "SOFTWARE_VERSION", "WEBSITE_ADDRESS", 
                      "DIGIT", "WS" ]

    RULE_start = 0
    RULE_nationalNumber = 1
    RULE_email = 2
    RULE_postalCode = 3
    RULE_decimalNumber = 4
    RULE_softwareVersion = 5
    RULE_websiteAddress = 6

    ruleNames =  [ "start", "nationalNumber", "email", "postalCode", "decimalNumber", 
                   "softwareVersion", "websiteAddress" ]

    EOF = Token.EOF
    EMAIL=1
    NATIONAL_NUMBER=2
    POSTAL_CODE=3
    DECIMAL_NUMBER=4
    SOFTWARE_VERSION=5
    WEBSITE_ADDRESS=6
    DIGIT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nationalNumber(self):
            return self.getTypedRuleContext(mainParser.NationalNumberContext,0)


        def email(self):
            return self.getTypedRuleContext(mainParser.EmailContext,0)


        def postalCode(self):
            return self.getTypedRuleContext(mainParser.PostalCodeContext,0)


        def decimalNumber(self):
            return self.getTypedRuleContext(mainParser.DecimalNumberContext,0)


        def softwareVersion(self):
            return self.getTypedRuleContext(mainParser.SoftwareVersionContext,0)


        def websiteAddress(self):
            return self.getTypedRuleContext(mainParser.WebsiteAddressContext,0)


        def EOF(self):
            return self.getToken(mainParser.EOF, 0)

        def getRuleIndex(self):
            return mainParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = mainParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.nationalNumber()
            self.state = 15
            self.email()
            self.state = 16
            self.postalCode()
            self.state = 17
            self.decimalNumber()
            self.state = 18
            self.softwareVersion()
            self.state = 19
            self.websiteAddress()
            self.state = 20
            self.match(mainParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NationalNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NATIONAL_NUMBER(self):
            return self.getToken(mainParser.NATIONAL_NUMBER, 0)

        def getRuleIndex(self):
            return mainParser.RULE_nationalNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNationalNumber" ):
                listener.enterNationalNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNationalNumber" ):
                listener.exitNationalNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNationalNumber" ):
                return visitor.visitNationalNumber(self)
            else:
                return visitor.visitChildren(self)




    def nationalNumber(self):

        localctx = mainParser.NationalNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nationalNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(mainParser.NATIONAL_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMAIL(self):
            return self.getToken(mainParser.EMAIL, 0)

        def getRuleIndex(self):
            return mainParser.RULE_email

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmail" ):
                listener.enterEmail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmail" ):
                listener.exitEmail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmail" ):
                return visitor.visitEmail(self)
            else:
                return visitor.visitChildren(self)




    def email(self):

        localctx = mainParser.EmailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_email)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(mainParser.EMAIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostalCodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSTAL_CODE(self):
            return self.getToken(mainParser.POSTAL_CODE, 0)

        def getRuleIndex(self):
            return mainParser.RULE_postalCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostalCode" ):
                listener.enterPostalCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostalCode" ):
                listener.exitPostalCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostalCode" ):
                return visitor.visitPostalCode(self)
            else:
                return visitor.visitChildren(self)




    def postalCode(self):

        localctx = mainParser.PostalCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_postalCode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(mainParser.POSTAL_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecimalNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_NUMBER(self):
            return self.getToken(mainParser.DECIMAL_NUMBER, 0)

        def getRuleIndex(self):
            return mainParser.RULE_decimalNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalNumber" ):
                listener.enterDecimalNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalNumber" ):
                listener.exitDecimalNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalNumber" ):
                return visitor.visitDecimalNumber(self)
            else:
                return visitor.visitChildren(self)




    def decimalNumber(self):

        localctx = mainParser.DecimalNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decimalNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(mainParser.DECIMAL_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SoftwareVersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SOFTWARE_VERSION(self):
            return self.getToken(mainParser.SOFTWARE_VERSION, 0)

        def getRuleIndex(self):
            return mainParser.RULE_softwareVersion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoftwareVersion" ):
                listener.enterSoftwareVersion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoftwareVersion" ):
                listener.exitSoftwareVersion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoftwareVersion" ):
                return visitor.visitSoftwareVersion(self)
            else:
                return visitor.visitChildren(self)




    def softwareVersion(self):

        localctx = mainParser.SoftwareVersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_softwareVersion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(mainParser.SOFTWARE_VERSION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WebsiteAddressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WEBSITE_ADDRESS(self):
            return self.getToken(mainParser.WEBSITE_ADDRESS, 0)

        def getRuleIndex(self):
            return mainParser.RULE_websiteAddress

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWebsiteAddress" ):
                listener.enterWebsiteAddress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWebsiteAddress" ):
                listener.exitWebsiteAddress(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWebsiteAddress" ):
                return visitor.visitWebsiteAddress(self)
            else:
                return visitor.visitChildren(self)




    def websiteAddress(self):

        localctx = mainParser.WebsiteAddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_websiteAddress)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(mainParser.WEBSITE_ADDRESS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





