# Basic Concepts for Initialization of UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.initio of UnivMathSys'''


from Elementary.build import FalseFunc
from Elementary.certify import Check
from Foundation.basic import MathBasic


class Variable(MathBasic):

    '''Concept Variable'''

    Definition = "Variable"
    Denotation = "\\mu"
    Formulation = Denotation
    Rpsntation = Denotation

    @property
    def Rpsnt(self):
        return self.Rpsntation

    @Rpsnt.setter
    def Rpsnt(self, NewRp):
        self.Rpsntation = NewRp


class Predicate(MathBasic):

    '''Concept Predicate'''

    Definition = "Predicate"
    Denotation = "\\mu"
    TruthValue = False
    Formulation = Denotation
    Conditioned = FalseFunc

    @property
    def Truth(self):
        return self.TruthValue

    @property
    def Condition(self):
        return self.Conditioned

    @Truth.setter
    def Truth(self, NewVal):
        Check(NewVal, bool)
        self.TruthValue = NewVal

    @Condition.setter
    def Condition(self, NewFunc):
        Check(NewFunc, 'function')
        self.Conditioned = NewFunc


class Class(MathBasic):

    '''Concept Class'''

    Definition = "Class"
    Denotation = "X"
    ObjectForm = Variable()
    Property = Predicate()
    Formulation = Denotation

    @property
    def Object(self):
        return self.ObjectForm

    @property
    def Prop(self):
        return self.Property

    @Object.setter
    def Object(self, NewObj):
        Check(NewObj, Variable)
        self.ObjectForm = NewObj
        Class.UpdateMathForm(self)

    @Prop.setter
    def Prop(self, NewProp):
        Check(NewProp, Predicate)
        self.Property = NewProp
        Class.UpdateMathForm(self)

    @staticmethod
    def UpdateMathForm(InClass):
        InClass.MathForm = "\\{" + \
            InClass.Object.Symbol
        InClass.MathForm += "\\mid "
        InClass.MathForm += \
            InClass.Prop.MathForm
        InClass.MathForm += "\\}"


class Object(MathBasic):

    '''Concept Object'''

    Definition = "Object"
    Denotation = "x"
    ClassForm = Class()
    Formulation = Denotation
    Property = ClassForm.Prop

    @property
    def ClsForm(self):
        return self.ClassForm

    @property
    def Prop(self):
        return self.Property

    @ClsForm.setter
    def ClsForm(self, NewCls):
        Check(NewCls, Class)
        self.ClassForm = NewCls
        self.Property = NewCls.Prop


class BelongTo(MathBasic):

    '''Operation Belong To'''

    Definition = "belong to"
    Denotation = "\\in"
    Formulation = Predicate()

    @classmethod
    def BelongsTo(Cls, InVar, InClass):
        TempPredicate = Predicate()
        TempPredicate.MathForm = \
            InVar.Symbol + \
            Cls.Denotation + \
            InClass.Symbol
        TempPredicate.TruthValue = \
            InClass.Prop.Condition\
                (InVar, InClass)
        return TempPredicate


# End of Module Foundation.initio of UnivMathSys
