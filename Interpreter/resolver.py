# Fundamental Formula Resolver for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Basic Formula Resolver of UnivMathSys'''


from Elementary.error import FormulaError
from Elementary.error import Insufficiency
from Elementary.syntr import BaseAST
from Interpreter.rslvlib import BasicFormulation
from Interpreter.rslvlib import BasicOperation
from Interpreter.rslvlib import Formulation

import re
import logging
from copy import deepcopy as clone
Logger = logging.getLogger('Resolver')


class FormulaAST(BaseAST):

    FORALL = r'(?P<FORALL>\\forall)'
    EXISTS = r'(?P<EXISTS>\\exists)'
    NEG = r'(?P<NEG>\\neg)'
    CONJUNC = r'(?P<CONJUNC>\\wedge)'
    DISJUNC = r'(?P<DISJUNC>\\vee)'

    OpList = [FORALL, EXISTS, NEG, CONJUNC, DISJUNC]
    IdList = OpList + BasicFormulation
    BscOpr = [re.compile(Op) for Op in BasicOperation]

    def Initio(self):
        Pattern = '|'.join(self.IdList) + '|'
        Pattern += self.Internal
        self._Pattern = re.compile(Pattern)

    def Resolve(self, Status, Property):
        self.StatList = None
        self.PropList = None
        self.Status = None
        self.Property = None
        if not Status or not Property:
            return False
        if not isinstance(Status, list):
            Status = [Status]
        if not isinstance(Property, list):
            Property = [Property]
        self.Separate(Status, Property)
        self.LinkTruth()
        TruthList = self.EnumTruth(len(self.StatList))
        for TruthConf in TruthList:
            Logger.debug("Truth Config: " + \
                str(TruthConf))
            for i in range(len(TruthConf)):
                self.StatList[i].Truth = TruthConf[i]
            Logger.debug("Status: " + \
                str(self.Status()) + " Property:"\
                    + " " + str(self.Property()))
            if self.Status():
                if not self.Property():
                    self.CheckSufficiency()
                    return False
        return True

    def Generate(self, Input):
        return self.Analyse(Input), self.FormulaList

    def Separate(self, Status, Property):

        def Assign(Type, Reslt, Prev):
            Relation = lambda: Reslt() and Prev()
            if Type == 'Status':
                self.Status = Relation
            else:
                self.Property = Relation

        for Stats in Status:
            Result = self.Analyse(Stats)
            self.FormulaList = Formulation.instances
            if not self.Status:
                self.Status = Result
                self.StatList = self.FormulaList
            else:
                PrevStats = self.Status
                Assign('Status', Result, PrevStats)
                self.StatList += self.FormulaList
        for Propty in Property:
            Result = self.Analyse(Propty)
            self.FormulaList = Formulation.instances
            if not self.Property:
                self.Property = Result
                self.PropList = self.FormulaList
            else:
                PrevProp = self.Property
                Assign('Propty', Result, PrevStats)
                self.PropList += self.FormulaList

        Logger.debug("Separate Result: \n" + \
            "Status List: \n" + str(self.StatList) + \
                "\n" + "Property List: \n" + \
                    str(self.PropList))

    def LinkTruth(self):
        Logger.info("Linking Truth")
        Logger.info("StatList: " + str(self.StatList))

        def Switch(Stats, Propty):
            if Stats.Tendency == Propty.Tendency:
                Propty.Truth = lambda: Stats.Truth
            else:
                Propty.Truth = lambda: not Stats.Truth

        for Stats in self.StatList:
            for Propty in self.PropList:
                if Stats == Propty:
                    Propty.Truth = lambda: Stats.Truth
                    continue
                for Op in self.BscOpr:
                    StMatch = Op.match(Stats.Formula)
                    PrMatch = Op.match(Propty.Formula)
                    if StMatch and PrMatch and \
                       StMatch.groups() == \
                       PrMatch.groups():
                        Switch(Stats, Propty)

    def CheckSufficiency(self):
        for Propty in self.PropList:
            if not callable(Propty.Truth):
                raise Insufficiency

    @staticmethod
    def EnumTruth(n):
        return [[bool(i&2**j) for j in range(n)]
                    for i in range(2**n)]

    def _Final(self):
        self.FormulaList = list()
        Formulation.Reset()
        Logger.info("Resolving Final Formula")
        return self.FinalFormula()

    def FinalFormula(self):
        Left = self.GenrlFormula()
        try:
            if self._Accept('CONJUNC'):
                Logger.info("Formula: Conjunction")
                Rght = self.GenrlFormula()
                Truth = lambda: Left() and Rght()
                while self._Accept('CONJUNC'):
                    Reslt = self.GenrlFormula()
                    PrevTruth = Truth
                    Truth = lambda: \
                        PrevTruth() and Reslt()
                return Truth
            elif self._Accept("DISJUNC"):
                Logger.info("Formula: Disjunction")
                Rght = self.GenrlFormula()
                Truth = lambda: Left() or Rght()
                while self._Accept('DISJUNC'):
                    Reslt = self.GenrlFormula()
                    PrevTruth = Truth
                    Truth = lambda: \
                        PrevTruth() or Reslt()
                return Truth
            else:
                raise FormulaError
        except FormulaError:
            return Left

    def GenrlFormula(self):
        if self._Accept('LPAREN'):
            Logger.info("Formula: Genrl -> Final")
            Truth = self.FinalFormula()
            self._Expect('RPAREN')
            return Truth
        elif self._Accept('NEG'):
            Logger.info("Formula: Genrl - Negation")
            Truth = self.GenrlFormula()
            return lambda: not Truth()
        else:
            Logger.info("Formula: Genrl -> Basic")
            return self.BasicFormula()

    def BasicFormula(self):
        Logger.info("Formula: Basic - " + \
            str(self.NextToken))
        if self._Accept('TRUEFORMULA'):
            CurrFormula = Formulation\
                (self.CurrToken.Value, False, True)
            return lambda: CurrFormula.Truth() \
                if callable(CurrFormula.Truth) else\
                    CurrFormula.Truth
        elif self._Accept('FALSEFORMULA'):
            CurrFormula = Formulation\
                (self.CurrToken.Value, False, False)
            return lambda: CurrFormula.Truth() \
                if callable(CurrFormula.Truth) else\
                    CurrFormula.Truth
        else:
            raise FormulaError

ResolveEngine = FormulaAST()


# End of Formula Resolver for UnivMathSys
