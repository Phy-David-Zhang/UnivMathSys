# Definition of Operations of Sets for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.setop of UnivMathSys'''


from Elementary.certify import Check
from Elementary.syntr import BaseAST
from Elementary.error import FormulaError
from Foundation.basic import Variable, Operator, \
    Morphism
from Foundation.logic import Neg, Conjunc, Disjunc
from Foundation.set import Set, Element, Subset, \
    SetEqual


class SetAST(BaseAST):

    UNION = r'(?P<UNION>\\cup)'
    INTSCT = r'(?P<INTSCT>\\cap)'
    COMPLT = r'(?P<COMPLT>\\complement)'
    CARTPROD = r'(?P<CARTPROD>\\times)'

    OpList = [UNION, INTSCT, COMPLT, CARTPROD]
    OpName = {'UNION': 'Union',
              'INTSCT': 'Intsct',
              'CARTPROD': 'CartProct'}

    def Initio(self):
        Pattern = '|'.join(self.OpList)
        super().Initio(Pattern)

    def _Final(self):
        return self.FinalSet()

    def FinalSet(self):
        if self._Accept('COMPLT'):
            self._Expect('UDLINE')
            Univ = self.GenrlSet()
            Input = self.GenrlSet()
            return "Complt(" + Univ + "," + \
                Input + ")"
        try:
            Left = self.GenrlSet()
            OpMatch = None
            OpFunc = None
            for Op, Val in self.OpName.items():
                if self._Accept(Op):
                    OpMatch = Op
                    OpFunc = self.OpName[Op]
            if not OpFunc:
                raise FormulaError
            Rght = self.GenrlSet()
            Formula = OpFunc + \
                "(" + Left + "," + Rght + ")"
            while self._Accept(OpMatch):
                Left = Formula
                Rght = self.GenrlSet()
                Formula = OpFunc + \
                    "(" + Left + "," + Rght + ")"
            return Formula
        except FormulaError:
            self._Restore()
            return self.BasicSet()

    def GenrlSet(self):
        if self._Accept('LPAREN'):
            Formula = self.FinalSet()
            self._Expect('RPAREN')
            return Formula
        else:
            return self.BasicSet()

    def BasicSet(self):
        if self._Accept('ID'):
            return self.CurrToken.Value


__OpList__ = ["\\cup", "\\cap", "\\complement",
              "\\times"]


class SetUnion(Operator):

    _Define = "Union"
    _Symbol = "\\cup"
    _OpList = __OpList__

    @staticmethod
    def Action(self, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)
        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Left, Rght])
        TempSet.Unique['Origin'] = lambda any: \
            self.Precdc(TempSet.Unique['Depend'][0]\
                .Symbol) + "\\cup " + self.Precdc(
            TempSet.Unique['Depend'][1].Symbol)
        TempSet.Symbol = \
            TempSet.Unique['Origin'](self)
        TempSet.Property = lambda self: Disjunc(
            TempSet.Unique['Depend'][0]\
                .Unique['Property'],
            TempSet.Unique['Depend'][1]\
                .Unique['Property'])._Format\
                    ([Left.Elmnt, TempSet.Elmnt] + \
                     [Rght.Elmnt, TempSet.Elmnt])
        TempSet.Unique['Property'].Short = lambda em:\
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][0].Symbol \
                    + "\\vee " + \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][1].Symbol
        return TempSet


class Intersection(Operator):

    _Define = "Intersection"
    _Symbol = "\\cap"
    _OpList = __OpList__

    @staticmethod
    def Action(self, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)
        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Left, Rght])
        TempSet.Unique['Origin'] = lambda any: \
            self.Precdc(TempSet.Unique['Depend'][0]\
                .Symbol) + "\\cap " + self.Precdc(
            TempSet.Unique['Depend'][1].Symbol)
        TempSet.Symbol = \
            TempSet.Unique['Origin'](self)
        TempSet.Property = lambda self: Conjunc(
            TempSet.Unique['Depend'][0]\
                .Unique['Property'],
            TempSet.Unique['Depend'][1]\
                .Unique['Property'])._Format\
                    ([Left.Elmnt, TempSet.Elmnt] + \
                     [Rght.Elmnt, TempSet.Elmnt])
        TempSet.Unique['Property'].Short = lambda em:\
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][0].Symbol \
                    + "\\wedge " + \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][1].Symbol
        return TempSet


class Complement(Operator):

    _Define = "Complement"
    _Symbol = "\\complement"

    @staticmethod
    def Action(self, Univ, Input):
        Check(Univ, Set)
        Check(Input, Set)
        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Univ, Input])
        TempSet.Unique['Origin'] = lambda any: \
            "\\complement_" + self.Precdc(
            TempSet.Unique['Depend'][0]\
                .Symbol) + " " + self.Precdc(
            TempSet.Unique['Depend'][1].Symbol)
        TempSet.Symbol = \
            TempSet.Unique['Origin'](self)
        TempSet.Property = lambda self: Conjunc(
            TempSet.Unique['Depend'][0]\
                .Unique['Property'], Neg(
            TempSet.Unique['Depend'][1]\
                .Unique['Property']))._Format\
                    ([Univ.Elmnt, TempSet.Elmnt] + \
                     [Input.Elmnt, TempSet.Elmnt])
        TempSet.Unique['Property'].Short = lambda em:\
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][0].Symbol \
                    + "\\wedge " + \
            TempSet.Elmnt + "\\notin " + \
                TempSet.Unique['Depend'][1].Symbol
        return TempSet


class CartesianProduct(Operator):

    _Define = "Cartesian Product"
    _Symbol = "\\times"

    @staticmethod
    def Action(self, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)
        TempSet = Set()
        TempSet.Elmnt = lambda self: "(" + \
            TempSet.Unique['Depend'][0].Elmnt + "," +\
            TempSet.Unique['Depend'][1].Elmnt + ")"
        TempSet.Unique['Depend'].extend([Left, Rght])
        TempSet.Unique['Origin'] = lambda self: \
            TempSet.Unique['Depend'][0].Symbol \
                + "\\times " + \
            TempSet.Unique['Depend'][1].Symbol
        TempSet.Symbol = \
            TempSet.Unique['Origin'](self)
        TempSet.Unique['Element'] = \
            (Element(TempSet.Unique['Depend'][0]),
             Element(TempSet.Unique['Depend'][1]))
        TempSet.Unique['Element'][0].Symbol = \
            TempSet.Unique['Depend'][0].Elmnt
        TempSet.Unique['Element'][1].Symbol = \
            TempSet.Unique['Depend'][1].Elmnt
        TempSet.Property = lambda self: \
            TempSet.Unique['Depend'][0].Elmnt \
                + "\\in " + \
            TempSet.Unique['Depend'][0].Symbol \
                + "\\wedge " + \
            TempSet.Unique['Depend'][1].Elmnt \
                + "\\in " + \
            TempSet.Unique['Depend'][1].Symbol
        return TempSet


def Contain(Left, Rght):
    OpContain = Subset()
    return OpContain(Left, Rght)

def SetEq(Left, Rght):
    OpSetEq = SetEqual()
    return OpSetEq(Left, Rght)

def Union(Left, Rght):
    OpUnion = SetUnion()
    return OpUnion(Left, Rght)

def Intsct(Left, Rght):
    OpIntersect = Intersection()
    return OpIntersect(Left, Rght)

def Complt(Univ, Input):
    OpComplt = Complement()
    return OpComplt(Univ, Input)

def CartProct(Left, Rght):
    OpCross = CartesianProduct()
    return OpCross(Left, Rght)


# End of Module Foundation.setop of UnivMathSys
