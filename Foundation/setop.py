# Definition of Operations of Sets for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.setop of UnivMathSys'''


from Elementary.certify import Check
from Foundation.basic import Variable, Operator, \
    Morphism
from Foundation.logic import Neg, Conjunc, Disjunc
from Foundation.set import Subclass, Set, \
    Element, SetEqual


class SetUnion(Operator):

    _Define = "Union"
    _Symbol = "\\cup"

    @staticmethod
    def Action(self, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)

        def Condition(InVar, InSet):
            return Disjunc(
                InVar.BelongTo(InSet\
                    .Unique['Depend'][0]),
                InVar.BelongTo(InSet\
                    .Unique['Depend'][1])
            ).Truth

        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Left, Rght])
        TempSet.Unique['Origin'] = lambda self: \
            TempSet.Unique['Depend'][0].Symbol \
                + "\\cup " + \
            TempSet.Unique['Depend'][1].Symbol
        TempSet.PropForm = lambda self: \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][0].Symbol \
                    + "\\vee " + \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][1].Symbol
        TempSet.Condition = Condition
        return TempSet


class Intersection(Operator):

    _Define = "Intersection"
    _Symbol = "\\cap"

    @staticmethod
    def Action(self, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)

        def Condition(InVar, InSet):
            return Conjunc(
                InVar.BelongTo(InSet\
                    .Unique['Depend'][0]),
                InVar.BelongTo(InSet\
                    .Unique['Depend'][1])
            ).Truth

        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Left, Rght])
        TempSet.Unique['Origin'] = lambda self: \
            TempSet.Unique['Depend'][0].Symbol \
                + "\\cap " + \
            TempSet.Unique['Depend'][1].Symbol
        TempSet.PropForm = lambda self: \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][0].Symbol \
                    + "\\wedge " + \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][1].Symbol
        TempSet.Condition = Condition
        return TempSet


class Complement(Operator):

    _Define = "Complement"
    _Symbol = "\\complement"

    @staticmethod
    def Action(self, Univ, Input):
        Check(Univ, Set)
        Check(Input, Set)

        def Condition(InVar, InSet):
            return Conjunc(
                InVar.BelongTo(InSet\
                    .Unique['Depend'][0]),
                Neg(InVar.BelongTo(InSet\
                    .Unique['Depend'][1]))
            ).Truth

        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Univ, Input])
        TempSet.Unique['Origin'] = lambda self: \
            "\\complement_" + \
            TempSet.Unique['Depend'][0].Symbol + \
            TempSet.Unique['Depend'][1].Symbol
        TempSet.PropForm = lambda self: \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][0].Symbol \
                    + "\\wedge " + \
            TempSet.Elmnt + "\\notin " + \
                TempSet.Unique['Depend'][1].Symbol
        TempSet.Condition = Condition
        return TempSet


def Contain(Left, Rght):
    OpContain = Subclass()
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


# End of Module Foundation.setop of UnivMathSys
