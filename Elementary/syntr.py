# Abstract Syntax Tree Template For UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Syntax Tree Template of UnivMathSys'''


import re
import logging
from collections import namedtuple

Logger = logging.getLogger('Main')


class BaseAST(object):

    ID = r'(?P<ID>[a-zA-Z][0-9a-zA-Z\_]*)'
    IID = r'(?:\s+|^)(?P<IID>\_[0-9a-zA-Z\_]*)'
    WS = r'(?P<WS>\s+)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<OPPLUS>\+)'
    MINUS = r'(?P<OPMINUS>-)'
    TIMES = r'(?P<OPTIMES>\*)'
    DIVIDE = r'(?P<OPDIVIDE>/)'
    LPAREN = r'(?P<LPAREN>\()'
    RPAREN = r'(?P<RPAREN>\))'
    UDLINE = r'(?P<UDLINE>_)'

    Internal = '|'.join([ID, WS, NUM, PLUS,
        MINUS, TIMES, DIVIDE, LPAREN, RPAREN, UDLINE])

    def __init__(self, *args, **kwargs):
        self._Pattern = self.Internal
        self.Initio(*args, **kwargs)

    def Initio(self, Pattern):
        self._Pattern += '|' + Pattern
        self._Pattern = re.compile(self._Pattern)

    def Analyse(self, Input):
        Logger.info("Enter Analyse")
        Logger.debug("Input: " + Input)
        self.TokenList = self.GenTokens(Input)
        self.PrevToken = None
        self.CurrToken = None
        self.NextToken = None
        self._Advance()
        Logger.info("Enter _Final")
        return self._Final()

    def GenTokens(self, text):
        Token = namedtuple('Token', ['Type', 'Value'])
        Scanner = self._Pattern.scanner(text)
        for m in iter(Scanner.match, None):
            Tokens = Token(m.lastgroup, m.group())
            if Tokens.Type != 'WS':
                Regret = yield Tokens
                if Regret:
                    yield None
                    Regret = yield Regret

    def _Advance(self):
        self.PrevToken, self.CurrToken, \
            self.NextToken = self.CurrToken, \
            self.NextToken, next(self.TokenList, None)
        Logger.info("Advance: " + str(self.CurrToken))

    def _Restore(self):
        if self.NextToken:
            self.TokenList.send(self.NextToken)
        self.CurrToken, self.NextToken = \
            self.PrevToken, self.CurrToken
        Logger.info("Restore: " + str(self.CurrToken))

    def _Accept(self, Type):
        if self.NextToken and \
                self.NextToken.Type == Type:
            self._Advance()
            Logger.debug("Accept: " + \
                str(self.CurrToken))
            return True
        else:
            return False

    def _Expect(self, Type):
        if not self._Accept(Type):
            raise SyntaxError("Unidentified " + \
                "Syntax: " + self.NextToken.Value)

    def _Final(self):
        pass


# End of Syntax Tree Template for UnivMathSys
