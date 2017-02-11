# Definition of Basic Set Theory for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.set of UnivMathSys'''


from Elementary.error import IllDefined, AccessError
from Elementary.certify import Check
from Foundation.basic import Variable, Operator, \
    Morphism
from Foundation.initio import Predicate, Class, \
    Object, BelongTo
from Foundation.logic import Imply


class Subclass(Operator):

    _Define = "Subclass"
    _Symbol = "\\subset"

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Class)
        Check(Rght, Class)
        TempPredicate.Format = \
            Left.Symbol + \
            self.Symbol + " " + \
            Rght.Symbol
        TempPredicate.Truth = Imply(
                Object(Left).BelongTo(Left), \
                Object(Left).BelongTo(Rght) \
            ).Truth
        return TempPredicate


class Set(Class):

    _Define = "Set"
    _Symbol = "X"
    _Element = "x"

    @Variable.UniqueInit
    def Initio(self):
        self._Symbol = "X"
        self._Format = self._Symbol
        self._Element = "x"
        self._Unique['Property'] \
            = Predicate()

    @property
    def Elmnt(self):
        return self._Element

    @Elmnt.setter
    def Elmnt(self, NewElm):
        self._Element = NewElm

    @staticmethod
    def DefCheck(Input):
        Check(Input, Set)
        TempVar = Object(Class())
        del TempVar.Status[:]
        if TempVar.BelongTo(Input):
            raise IllDefined

    @property
    def Property(self):
        raise AccessError("Access Denied")

    @property
    def PropForm(self):
        return self._Unique['Property'].Format

    @property
    def Condition(self):
        return self._Unique['Property'].Condition

    @Property.setter
    def Property(self, NewProp):
        Check(NewProp, Predicate)
        self.PropForm = NewProp.Format
        self.Condition = NewProp.Condition

    @PropForm.setter
    def PropForm(self, NewForm):
        Check(NewForm, str)
        self._Unique['Property'].Format = NewForm
        self._Unique['Sync'] = False
        Class.UpdateFormat(self)

    @Condition.setter
    def Condition(self, NewFunc):
        Check(NewFunc, 'function')
        TempFunc = self.Condition
        self._Unique['Property'].Condition = NewFunc
        try:
            Set.DefCheck(self)
        except IllDefined:
            print("Set Property Invalid: " + \
                "Probable Russell Set")
            self._Unique['Property']\
                .Condition = TempFunc


class Element(Object):

    _Define = "Element"
    _Symbol = "x"
    _Format = _Symbol

    @Variable.UniqueInit
    def Initio(self, InSet, InVar=None):
        if InVar is not None:
            Check(InVar, Variable)
            self.Symbol = InVar.Symbol
            self.Unique = InVar.Unique
        Check(InSet, Set)
        self.Status = InSet.Symbol
        self.Status = InSet.PropForm


class SetEqual(Operator):

    _Define = "equal"
    _Symbol = {False:"\\neq ", True:"="}

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Set)
        Check(Rght, Set)
        Op = Subclass()
        TempPredicate.Truth = \
            Subclass.Action(Op, Left, Rght).Truth \
            and Subclass.Action(Op, Rght, Left).Truth
        TempPredicate.Format = \
            Left.Symbol + \
            self.Symbol[TempPredicate.Truth] + \
            Rght.Symbol
        return TempPredicate


# End of Module Foundation.set of UnivMathSys
