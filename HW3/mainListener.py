# Generated from C:/Users/black/compiler_design_fall_2023/HW4/HW3/main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete listener for a parse tree produced by mainParser.
class mainListener(ParseTreeListener):

    # Enter a parse tree produced by mainParser#start.
    def enterStart(self, ctx:mainParser.StartContext):
        pass

    # Exit a parse tree produced by mainParser#start.
    def exitStart(self, ctx:mainParser.StartContext):
        pass


    # Enter a parse tree produced by mainParser#nationalNumber.
    def enterNationalNumber(self, ctx:mainParser.NationalNumberContext):
        pass

    # Exit a parse tree produced by mainParser#nationalNumber.
    def exitNationalNumber(self, ctx:mainParser.NationalNumberContext):
        pass


    # Enter a parse tree produced by mainParser#email.
    def enterEmail(self, ctx:mainParser.EmailContext):
        pass

    # Exit a parse tree produced by mainParser#email.
    def exitEmail(self, ctx:mainParser.EmailContext):
        pass


    # Enter a parse tree produced by mainParser#postalCode.
    def enterPostalCode(self, ctx:mainParser.PostalCodeContext):
        pass

    # Exit a parse tree produced by mainParser#postalCode.
    def exitPostalCode(self, ctx:mainParser.PostalCodeContext):
        pass


    # Enter a parse tree produced by mainParser#decimalNumber.
    def enterDecimalNumber(self, ctx:mainParser.DecimalNumberContext):
        pass

    # Exit a parse tree produced by mainParser#decimalNumber.
    def exitDecimalNumber(self, ctx:mainParser.DecimalNumberContext):
        pass


    # Enter a parse tree produced by mainParser#softwareVersion.
    def enterSoftwareVersion(self, ctx:mainParser.SoftwareVersionContext):
        pass

    # Exit a parse tree produced by mainParser#softwareVersion.
    def exitSoftwareVersion(self, ctx:mainParser.SoftwareVersionContext):
        pass


    # Enter a parse tree produced by mainParser#websiteAddress.
    def enterWebsiteAddress(self, ctx:mainParser.WebsiteAddressContext):
        pass

    # Exit a parse tree produced by mainParser#websiteAddress.
    def exitWebsiteAddress(self, ctx:mainParser.WebsiteAddressContext):
        pass



del mainParser