# Generated from C:/Users/black/compiler_design_fall_2023/HW4/Password.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PasswordParser import PasswordParser
else:
    from PasswordParser import PasswordParser

# This class defines a complete listener for a parse tree produced by PasswordParser.
class PasswordListener(ParseTreeListener):

    # Enter a parse tree produced by PasswordParser#password.
    def enterPassword(self, ctx:PasswordParser.PasswordContext):
        pass

    # Exit a parse tree produced by PasswordParser#password.
    def exitPassword(self, ctx:PasswordParser.PasswordContext):
        pass



del PasswordParser