# _Define of Propositional Logic for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.logic of UnivMathSys'''


from Elementary.error import LogicError
from Elementary.certify import Check
from Foundation.basic import Variable, Operator, \
    Morphism
from Foundation.initio import Predicate


class Negation(Operator):

    '''Concept Negation'''

    _Define = "Negation"
    _Symbol = "\\neg"

    @staticmethod
    def Action(self, Input):
        TempPredicate = Predicate()
        Check(Input, Predicate)
        TempPredicate.Format = \
            self.Symbol + " " + \
            Input.Symbol
        TempPredicate.Truth = \
            not Input.Truth
        return TempPredicate


class Conjunction(Operator):

    '''Concept Conjunction'''

    _Define = "Conjunction"
    _Symbol = "\\wedge"

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Predicate)
        Check(Rght, Predicate)
        TempPredicate.Format = \
            Left.Symbol + \
            self.Symbol+ " " + \
            Rght.Symbol
        TempPredicate.Truth = \
            Left.Truth and \
            Rght.Truth
        return TempPredicate


class Disjunction(Operator):

    '''Concept Disjunction'''

    _Define = "Disjunction"
    _Symbol = "\\vee"

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
            Left.Truth or \
            Rght.Truth
        return TempPredicate


class Implication(Operator):

    '''Concept Implication'''

    _Define = "Implication"
    _Symbol = "\\rightarrow"

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
