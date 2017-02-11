# Basic Concepts for Initialization of UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.initio of UnivMathSys'''


from Elementary.build import FalseFunc
from Elementary.certify import Check
from Foundation.basic import Variable, Operator, \
    Morphism


class Predicate(Variable):

    '''Concept Predicate'''

    _Define = "Predicate"
    _Symbol = "\\mu"
    _Format = _Symbol
    _Truth = False
    _Condition = FalseFunc

    @Variable.UniqueInit
    def Initio(self):
        self._Symbol = "\\mu"
        self._Truth = False
        self._Format = self._Symbol
        self._Condition = FalseFunc

    @Variable.Format.setter
    def Format(self, NewExp):
        self._Format = NewExp
        self._Unique['Sync'] = False

    @property
    def Truth(self):
        return self._Truth

    @property
    def Condition(self):
        return self._Condition

    @Truth.setter
    def Truth(self, NewVal):
        Check(NewVal, bool)
        self._Truth = NewVal

    @Condition.setter
    def Condition(self, NewFunc):
        Check(NewFunc, 'function')
        self._Condition = NewFunc


class Class(Variable):

    '''Concept Class'''

    _Define = "Class"
    _Symbol = "X"
    _Format = _Symbol
    _Object = "x"

    @Variable.UniqueInit
    def Initio(self):
        self._Symbol = "X"
        self._Format = self._Symbol
        self._Object = "x"
        self._Unique['Property'] \
            = Predicate()

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, NewObj):
        self._Object = NewObj
        Class.UpdateFormat(self)

    @Variable.Unique.setter
    def Unique(self, NewUnq):
        self._Unique.update(NewUnq)
        self._Unique['Sync'] = False
        Class.UpdateFormat(self)

    @staticmethod
    def UpdateFormat(InClass):
        InClass.Format = "\\{" + \
            InClass.Object
        InClass.Format += "\\mid "
        InClass.Format += \
            InClass.Unique['Property'].Format
        InClass.Format += "\\}"


class Object(Variable):

    '''Concept Object'''

    _Define = "Object"
    _Symbol = "x"
    _Format = _Symbol

    @Variable.UniqueInit
    def Initio(self, InClass, InVar=None):
        if InVar is not None:
            Check(InVar, Variable)
            self.Symbol = InVar.Symbol
            self.Unique = InVar.Unique
        Check(InClass, Class)
        self.Status = InClass.Symbol
        self.Status = InClass\
            .Unique['Property'].Format

    @Variable.Format.setter
    def Format(self, NewExp):
        self._Format = NewExp
        self._Unique['Sync'] = False

    def BelongTo(self, InClass):
        TempPredicate = Predicate()
        Check(InClass, Class)
        TempPredicate.Format = \
            self.Symbol + \
            "\\in" + " " + \
            InClass.Symbol
        TempPredicate.Truth = \
            InClass.Unique['Property'].\
                Condition(self, InClass)
        return TempPredicate


class BelongTo(Operator):

    '''Operator Belong To'''

    _Define = "belong to"
    _Symbol = "\\in"

    @staticmethod
    def Action(self, InVar, InClass):
        TempPredicate = Predicate()
        Check(InVar, Variable)
        Check(InClass, Class)
        TempPredicate.Format = \
            InVar.Symbol + \
            self.Symbol + " " + \
            InClass.Symbol
        TempPredicate.Truth = \
            InClass.Unique['Property'].\
                Condition(InVar, InClass)
        return TempPredicate


# End of Module Foundation.initio of UnivMathSys
