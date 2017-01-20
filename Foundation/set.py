# Definition of Propositional Logic for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.logic of UnivMathSys'''


from Elementary.error import IllDefined
from Elementary.certify import Check
from Foundation.basic import MathBasic
from Foundation.initio import Variable, Predicate, \
    Class, Object, BelongTo
from Foundation.logic import Implication


class Subclass(Class):

    Definition = "Subclass"
    Denotation = "\\subset"

    @classmethod
    def Contain(Cls, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Class)
        Check(Rght, Class)
        TempPredicate.MathForm = \
            Left.Symbol + \
            Cls.Denotation + " " + \
            Rght.Symbol
        TempPredicate.Truth = \
            Implication.Imply(
            BelongTo.BelongsTo \
                (Left.Object, Left), \
            BelongTo.BelongsTo \
                (Left.Object, Rght)).Truth
        return TempPredicate


class Set(Class):

    Definition = "Set"
    Denotation = "X"
    Element = Class.ObjectForm

    @staticmethod
    def Initio(self):
        self.Symbol = "X"
        self.MathForm = self.Symbol
        self.Elmnt = Variable()
        self.Prop = Predicate()

    @property
    def Elmnt(self):
        return self.Element

    @Elmnt.setter
    def Elmnt(self, NewElm):
        self.Object = NewElm
        self.Element = self.Object

    @staticmethod
    def DefCheck(Input):
        Check(Input, Set)
        TempVar = Variable()
        TempVar.Symbol = "0"
        TempVar.Rpsnt = None
        if BelongTo.BelongsTo \
            (TempVar, Input).Truth:
            raise IllDefined("Set Property Invalid")

    @Class.Prop.setter
    def Prop(self, NewProp):
        Check(NewProp, Predicate)
        TempProp = self.Prop
        self.Property = NewProp
        try:
            Set.DefCheck(self)
        except IllDefined:
            print("Set Property Invalid: " + \
                "Probable Russell Set")
            self.Property = TempProp
        Class.UpdateMathForm(self)


class Element(Object):

    Definition = "Element"
    Denotation = "x"
    TheSetForm = Object.ClassForm

    @staticmethod
    def Initio(self):
        self.Symbol = "x"
        self.MathForm = self.Symbol
        self.SetForm = Set()

    @property
    def SetForm(self):
        return self.TheSetForm

    @SetForm.setter
    def SetForm(self, NewSet):
        self.ClsForm = NewSet
        self.TheSetForm = self.ClassForm


class SetEqual(MathBasic):

    Definition = "equal"
    Denotation = {False:"\\neq ", True:"="}

    @classmethod
    def Equal(Cls, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Set)
        Check(Rght, Set)
        TempPredicate.Truth = \
            Subclass.Contain(Left, Rght).Truth \
            and Subclass.Contain(Rght, Left).Truth
        TempPredicate.MathForm = \
            Left.Symbol + \
            Cls.Denotation[TempPredicate.Truth] + \
            Rght.Symbol
        return TempPredicate

# End of Module Foundation.set of UnivMathSys
