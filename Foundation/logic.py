# Definition of Propositional Logic for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.logic of UnivMathSys'''


from Elementary.error import LogicError
from Elementary.certify import Check
from Foundation.basic import MathBasic
from Foundation.initio import Predicate


class Negation(MathBasic):

    '''Concept Negation'''

    Definition = "Negation"
    Denotation = "\\neg"

    @classmethod
    def Neg(Cls, Input):
        TempPredicate = Predicate()
        Check(Input, Predicate)
        TempPredicate.MathForm = \
            Cls.Denotation + " " + \
            Input.Symbol
        TempPredicate.TruthValue = \
            not Input.TruthValue
        return TempPredicate


class Conjunction(MathBasic):

    '''Concept Conjunction'''

    Definition = "Conjunction"
    Denotation = "\\wedge"

    @classmethod
    def Conjunc(Cls, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Predicate)
        Check(Rght, Predicate)
        TempPredicate.MathForm = \
            Left.Symbol + \
            Cls.Denotation + " " + \
            Rght.Symbol
        TempPredicate.TruthValue = \
            Left.TruthValue and \
            Rght.TruthValue
        return TempPredicate


class Disjunction(MathBasic):

    '''Concept Disjunction'''

    Definition = "Disjunction"
    Denotation = "\\vee"

    @classmethod
    def Disjunc(Cls, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Predicate)
        Check(Rght, Predicate)
        TempPredicate.MathForm = \
            Left.Symbol + \
            Cls.Denotation + " " + \
            Rght.Symbol
        TempPredicate.TruthValue = \
            Left.TruthValue or \
            Rght.TruthValue
        return TempPredicate

class Implication(MathBasic):

    '''Concept Implication'''

    Definition = "Implication"
    Denotation = "\\rightarrow"

    @classmethod
    def Imply(Cls, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Predicate)
        Check(Rght, Predicate)
        TempPredicate.MathForm = \
            Left.Symbol + \
            Cls.Denotation + " " + \
            Rght.Symbol
        TempPredicate.TruthValue = \
            (not Left.TruthValue) \
            or Rght.TruthValue
        return TempPredicate

    @classmethod
    def Check(Cls, Input):
        if Input.TruthValue == False:
            raise LogicError("Implication Error")

# End of Module Foundation.logic of UnivMathSys
