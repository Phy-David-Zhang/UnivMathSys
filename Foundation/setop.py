# Definition of Operations of Sets for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.setop of UnivMathSys'''


from Elementary.certify import Check
from Foundation.basic import MathBasic
from Foundation.initio import Variable, BelongTo
from Foundation.logic import Negation, \
    Conjunction, Disjunction


class Union(MathBasic):

    Definition = "Union"
    Denotation = "\\cup"

    @classmethod
    def Union(Cls, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)

        def Condition(InVar, InClass):
            return Disjunction.Disjunc(
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Left), \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Rght)).Truth

        TempSet = Set()
        TempSet.MathForm = Left.Symbol + \
            Cls.Symbol + Rght.Symbol
        TempSet.PropForm =
            Disjunction.Disjunc( \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Left), \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Rght)) \
            .MathForm
        TempSet.Condition = Condition


class Intersection(MathBasic):

    Definition = "Intersection"
    Denotation = "\\cap"

    @classmethod
    def Intersect(Cls, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)

        def Condition(InVar, InClass):
            return Conjunction.Conjunc(
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Left), \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Rght)).Truth

        TempSet = Set()
        TempSet.MathForm = Left.Symbol + \
            Cls.Symbol + Rght.Symbol
        TempSet.PropForm =
            Conjunction.Conjunc( \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Left), \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Rght)) \
            .MathForm
        TempSet.Condition = Condition


class Complement(MathBasic):

    Definition = "Complement"
    Denotation = "\\complement"

    @classmethod
    def Complt(Cls, Input, Univ):
        Check(Input, Set)
        Check(Univ, Set)

        def Condition(InVar, InClass):
            return Conjunction.Conjunc(
                Negation.Neg(
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Input)), \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Univ)).Truth

        TempSet = Set()
        TempSet.MathForm = Left.Symbol + \
            Cls.Symbol + Rght.Symbol
        TempSet.PropForm =
            Conjunction.Conjunc(
                Negation.Neg(
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Input)), \
                BelongTo.BelongsTo \
                    (TempSet.Elmnt, Univ)) \
            .MathForm
        TempSet.Condition = Condition

# End of Module Foundation.setop of UnivMathSys
