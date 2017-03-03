# Abstract Syntax Tree Template For UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Syntax Tree Template of UnivMathSys'''


import re
from collections import namedtuple


class BaseAST(object):

    def __init__(self, *args, **kwargs):
        self.Initio(self, *args, **kwargs)

    def Initio(self, Pattern):
        self._Pattern = re.compile(Pattern)

    def Analyse(self, Input):
        self.TokenList = GenTokens(Input)
        self.CurrToken = None
        self.NextToken = None
        self._Advance()
        return self._Final()

    def GenTokens(text):
        Token = namedtuple('Token', ['Type', 'Value'])
        Scanner = self._Pattern
        for m in iter(Scanner.match, None):
            Tokens = Token(m.lastgroup, m.group())
            if Tokens.Type != 'WS':
                yield Tokens

    def _Advance(self):
        self.CurrToken, self.NextToken = \
            self.NextToken, next(self.TokenList, None)

    def _Accept(self, Type):
        if self.NextToken and \
            self.NextToken.Type == Type:
            self._Advance()
            return True
        else:
            return False

    def _Expect(self, Type):
        if not self._Accept(Type):
            raise SyntaxError("Unidentified" + \
                "Syntax: " + self.NextToken)


# End of Syntax Tree Template for UnivMathSys
