# Definition of Propositional Logic for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.logic of UnivMathSys'''


from Elementary.error import LogicError
from Elementary.certify import Check
from Foundation.basic import Variable, Operator, \
    Morphism
from Foundation.initio import Predicate


__OpList__ = ["\\forall", "\\exists", "\\neg",
              "\\wedge", "\\vee", "\\Rightarrow"]


class UnivQuan(Operator):

    '''Concept Universal Quantifier'''

    _Define = "Universal Quantifier"
    _Symbol = "\\forall"

    @staticmethod
    def Action(self, InVar):
        Check(InVar, Variable)
        if 'Value' in InVar.Unique:
            del InVar.Unique['Value']


class ExistQuan(Operator):

    '''Concept Existential Quantifier'''

    _Define = "Existential Quantifier"
    _Symbol = "\\exists"

    @staticmethod
    def Action(self, InVar):
        Check(InVar, Variable)
        if not 'Value' in InVar.Unique:
            InVar.Unique = dict(Value=None)


class Negation(Operator):

    '''Concept Negation'''

    _Define = "Negation"
    _Symbol = "\\neg"

    @staticmethod
    def Action(self, Input):
        TempPredicate = Predicate()
        Check(Input, Predicate)
        TempPredicate.Format = \
            lambda any: \
                self.Symbol + " " + \
                self.Precdc(Input.Format) \
            if not isinstance(any, list) else \
                self.Symbol + " " + \
                self.Replace(any[0], any[1],
                    self.Precdc(Input.Format))
        TempPredicate.Truth = not Input.Truth
        return TempPredicate


class Conjunction(Operator):

    '''Concept Conjunction'''

    _Define = "Conjunction"
    _Symbol = "\\wedge"
    _OpList = __OpList__

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Predicate)
        Check(Rght, Predicate)
        TempPredicate.Format = \
            lambda any: \
                self.Precdc(Left.Format) + \
                self.Symbol + " " + \
                self.Precdc(Rght.Format) \
            if not isinstance(any, list) else \
                self.Replace(any[0], any[1],
                    self.Precdc(Left.Format)) + \
                self.Symbol + " " + \
                self.Replace(any[2], any[3],
                    self.Precdc(Rght.Format))
        TempPredicate.Truth = \
            Left.Truth and Rght.Truth
        return TempPredicate


class Disjunction(Operator):

    '''Concept Disjunction'''

    _Define = "Disjunction"
    _Symbol = "\\vee"
    _OpList = __OpList__

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Predicate)
        Check(Rght, Predicate)
        TempPredicate.Format = \
            lambda any: \
                self.Precdc(Left.Format) + \
                self.Symbol + " " + \
                self.Precdc(Rght.Format) \
            if not isinstance(any, list) else \
                self.Replace(any[0], any[1],
                    self.Precdc(Left.Format)) + \
                self.Symbol + " " + \
                self.Replace(any[2], any[3],
                    self.Precdc(Rght.Format))
        TempPredicate.Truth = \
            Left.Truth or Rght.Truth
        return TempPredicate


class Implication(Operator):

    '''Concept Implication'''

    _Define = "Implication"
    _Symbol = "\\Rightarrow"

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Predicate)
        Check(Rght, Predicate)
        TempPredicate.Format = \
            Left.Symbol + \
            self.Symbol + " " + \
            Rght.Symbol
        TempPredicate.Truth = \
            (not Left.Truth) \
            or Rght.Truth
        return TempPredicate

    @classmethod
    def Check(Cls, Input):
        if Input.Truth == False:
            raise LogicError("Implication Error")


def ForAll(InVar):
    OpForAll = UnivQuan()
    OpForAll(InVar)

def Exist(InVar):
    OpExist = ExistQuan()
    OpExist(InVar)

def Neg(Input):
    OpNot = Negation()
    return OpNot(Input)

def Conjunc(Left, Rght):
    OpWedge = Conjunction()
    return OpWedge(Left, Rght)

def Disjunc(Left, Rght):
    OpVee = Disjunction()
    return OpVee(Left, Rght)

def Imply(Left, Rght):
    OpArrow = Implication()
    return OpArrow(Left, Rght)


# End of Module Foundation.logic of UnivMathSys
