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
        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Left, Rght])
        TempSet.Unique['Origin'] = lambda self: \
            TempSet.Unique['Depend'][0].Symbol \
                + "\\cup " + \
            TempSet.Unique['Depend'][1].Symbol
        TempSet.Property = lambda self: \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][0].Symbol \
                    + "\\vee " + \
            TempSet.Elmnt + "\\in " + \
                TempSet.Unique['Depend'][1].Symbol
        return TempSet


class Intersection(Operator):

    _Define = "Intersection"
    _Symbol = "\\cap"

    @staticmethod
    def Action(self, Left, Rght):
        Check(Left, Set)
        Check(Rght, Set)
        TempSet = Set()
        TempSet.Unique['Depend']\
            .extend([Left, Rght])
        TempSet.Unique['Origin'] = lambda self: \
            TempSet.Unique['Depend'][0].Symbol \
                + "\\cap " + \
            TempSet.Unique['Depend'][1].Symbol
        TempSet.Property = lambda self: \
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
        TempSet.Unique['Origin'] = lambda self: \
            "\\complement_" + \
            TempSet.Unique['Depend'][0].Symbol + \
            TempSet.Unique['Depend'][1].Symbol
        TempSet.Property = lambda self: \
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

def CartProct(Left, Rght):
    OpCross = CartesianProduct()
    return OpCross(Left, Rght)


# End of Module Foundation.setop of UnivMathSys
