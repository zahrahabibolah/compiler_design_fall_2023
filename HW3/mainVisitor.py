# Generated from C:/Users/black/compiler_design_fall_2023/HW4/HW3/main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete generic visitor for a parse tree produced by mainParser.

class mainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mainParser#start.
    def visitStart(self, ctx:mainParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#nationalNumber.
    def visitNationalNumber(self, ctx:mainParser.NationalNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#email.
    def visitEmail(self, ctx:mainParser.EmailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#postalCode.
    def visitPostalCode(self, ctx:mainParser.PostalCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#decimalNumber.
    def visitDecimalNumber(self, ctx:mainParser.DecimalNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#softwareVersion.
    def visitSoftwareVersion(self, ctx:mainParser.SoftwareVersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#websiteAddress.
    def visitWebsiteAddress(self, ctx:mainParser.WebsiteAddressContext):
        return self.visitChildren(ctx)



del mainParser