# TestRun File of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Test Operating File of UnivMathSys'''


from Foundation.basic import MathBasic
from Elementary.build import TrueFunc, FalseFunc
from Elementary.certify import Check
from Foundation.initio import Variable, Predicate,\
    Class, Object, BelongTo
from Foundation.logic import Negation, Conjunction, \
    Disjunction, Implication
from Foundation.set import Subclass, Set, Element, \
    SetEqual


def Test_Foundation_initio_Variable():

    print("\nTest of Variable:")
    TestVar = Variable()
    TestVar.Symbol = "\\varphi"
    TestVar.Rpsnt = "Test String"
    print(TestVar.Define)
    print(TestVar.Symbol)
    print(TestVar.MathForm)
    print(TestVar.Rpsnt)


def Test_Foundation_initio_Predicate():

    print("\nTest of Predicate")
    TestPredicate = Predicate()
    TestPredicate.Symbol = "\\xi"
    TestPredicate.TruthValue = True
    TestPredicate.Condition = TrueFunc
    print(TestPredicate.Define)
    print(TestPredicate.Symbol)
    print(TestPredicate.MathForm)
    print(TestPredicate.TruthValue)
    print(TestPredicate.Condition())


def Test_Foundation_initio_Class():

    print("\nTest of Class")

    TestClass = Class()
    TestVar = Variable()
    TestPredicate = Predicate()

    TestVar.Symbol = "y"
    TestVar.MathForm = TestVar.Symbol

    TestPredicate.Symbol = "P(y)"
    TestPredicate.MathForm = "P(y)"
    TestPredicate.Condition = TrueFunc

    TestClass.Symbol = "Y"
    TestClass.Object = TestVar
    TestClass.Prop = TestPredicate

    print(TestClass.Define)
    print(TestClass.Symbol)
    print(TestClass.MathForm)
    print(TestClass.Prop.Condition())


def Test_Foundation_initio_Object():

    print("\nTest of Object")

    TestObject = Object()
    TestClass = Class()
    TestVar = Variable()
    TestPredicate = Predicate()

    TestVar.Symbol = "y"
    TestVar.MathForm = TestVar.Symbol

    TestPredicate.Symbol = "P(y)"
    TestPredicate.MathForm = "P(y)"
    TestPredicate.Condition = TrueFunc

    TestClass.Symbol = "Y"
    TestClass.Object = TestVar
    TestClass.Prop = TestPredicate

    TestObject.Symbol = "z"
    TestObject.MathForm = "z"
    TestObject.ClsForm = TestClass

    print(TestObject.Define)
    print(TestObject.Symbol)
    print(TestObject.MathForm)
    print(TestObject.ClsForm.MathForm)


def Test_Foundation_initio_BelongTo():

    print("\nTest of BelongTo")

    Belongto = BelongTo()
    TestObject = Variable()
    TestObjectF = Variable()
    TestClass = Class()
    TestVar = Variable()
    TestPredicate = Predicate()

    def TempFunc(InVar, InClass):
        return InVar.Symbol == InClass.Object.Symbol

    TestVar.Symbol = "y"
    TestVar.MathForm = TestVar.Symbol

    TestPredicate.Symbol = "P(y)"
    TestPredicate.MathForm = "P(y)"
    TestPredicate.Condition = TempFunc

    TestClass.Symbol = "Y"
    TestClass.Object = TestVar
    TestClass.Prop = TestPredicate

    TestObject.Symbol = "y"
    TestObject.MathForm = "y"

    print(Belongto.Define)
    print(Belongto.Symbol)
    print(BelongTo.BelongsTo(TestObject, TestClass).TruthValue)
    print(BelongTo.BelongsTo(TestObjectF, TestClass).TruthValue)


def Test_Foundation_logic_Negation():

    print("\nTest of Negation")

    TestPredicate = Predicate()
    print(TestPredicate.MathForm, TestPredicate.Truth)
    print(Negation.Neg(TestPredicate).MathForm, \
          Negation.Neg(TestPredicate).Truth)


def Test_Foundation_logic_Conjunction():

    print("\nTest of Conjunction")

    TestPredicateA = Predicate()
    TestPredicateB = Predicate()

    TestPredicateA.Truth = True
    Result = Conjunction.Conjunc(TestPredicateA, \
            TestPredicateB)

    print(Result.MathForm, Result.Truth)

    TestPredicateB.Truth = True
    Result = Conjunction.Conjunc(TestPredicateA, \
            TestPredicateB)

    print(Result.MathForm, Result.Truth)


def Test_Foundation_logic_Disjunction():

    print("\nTest of Disjunction")

    TestPredicateA = Predicate()
    TestPredicateB = Predicate()

    TestPredicateA.Truth = True
    Result = Disjunction.Disjunc(TestPredicateA, \
            TestPredicateB)

    print(Result.MathForm, Result.Truth)

    TestPredicateB.Truth = True
    Result = Disjunction.Disjunc(TestPredicateA, \
            TestPredicateB)

    print(Result.MathForm, Result.Truth)


def Test_Foundation_logic_Implication():

    print("\nTest of Implication")

    TestPredicateA = Predicate()
    TestPredicateB = Predicate()

    Result = Implication.Imply(TestPredicateA, \
            TestPredicateB)
    print(Result.MathForm, Result.Truth)

    TestPredicateA.Truth = True
    Result = Implication.Imply(TestPredicateA, \
            TestPredicateB)

    print(Result.MathForm, Result.Truth)

    TestPredicateB.Truth = True
    Result = Implication.Imply(TestPredicateA, \
            TestPredicateB)

    print(Result.MathForm, Result.Truth)


def Test_Foundation_set_Subclass():

    print("\nTest of Subclass")

    TestClass = Class()
    TestVar = Variable()
    TestPredicate = Predicate()

    def TempFunc(InVar, InClass):
        return InVar.Symbol == InClass.Object.Symbol

    TestVar.Symbol = "y"
    TestVar.MathForm = TestVar.Symbol

    TestPredicate.Symbol = "P(y)"
    TestPredicate.MathForm = "P(y)"
    TestPredicate.Condition = TempFunc

    TestClass.Symbol = "Y"
    TestClass.Object = TestVar
    TestClass.Prop = TestPredicate

    TempPredicate = Subclass.Contain \
        (TestClass, TestClass)

    print(TempPredicate.MathForm, TempPredicate.Truth)


def Test_Foundation_set_Set():

    print("\nTest of Set")

    TempSet = Set()
    TempPropA = Predicate()
    TempSet.Prop = TempPropA

    print(TempSet.Define, TempSet.Symbol, \
            TempSet.MathForm)

    def RussellCondition(InVar, InSet):
        Check(InVar, Variable)
        Check(InSet, Set)
        return not InVar.Rpsnt == InSet.Elmnt

    TempPropB = Predicate()
    TempPropB.Condition = RussellCondition
    TempPropB.MathForm = "x\\notin x"
    TempSet.Prop = TempPropB

    print(TempSet.Define, TempSet.Symbol, \
            TempSet.MathForm)

    TempPropC = Predicate()
    TempPropC.Condition = TrueFunc
    TempPropC.MathForm = "true"
    TempSet.Prop = TempPropC

    print(TempSet.Define, TempSet.Symbol, \
            TempSet.MathForm)


def Test_Foundation_set_Element():

    print("\nTest of Element")

    TempProp = Predicate()
    TempProp.MathForm = "false"
    TempSet = Set()
    TempSet.Prop = TempProp
    TempElement = Element()

    print(TempElement.Define, TempElement.Symbol)

    print(TempElement.SetForm.MathForm)

    TempElement.SetForm = TempSet

    print(TempElement.SetForm.MathForm)


def Test_Foundation_set_SetEqual():

    print("\nTest of SetEqual")

    TempSetA = Set()
    TempSetB = Set()

    def TempFunc(InVar, InClass):
        return InVar.Symbol == InClass.Object.Symbol

    TempPredicate = Predicate()
    TempPredicate.Condition = TempFunc
    TempSetB.Prop = TempPredicate
    TempVar = Variable()
    TempSetB.Elmnt = TempVar
    TempSetB.Symbol = "Y"

    TempPredicate = SetEqual.Equal(TempSetA, TempSetA)
    print(TempPredicate.MathForm, TempPredicate.Truth)

    TempPredicate = SetEqual.Equal(TempSetA, TempSetB)
    print(TempPredicate.MathForm, TempPredicate.Truth)


def TestRun():

    print(" ")
    print("Test for Universal Mathematics System")

    Test_Foundation_initio_Variable()
    Test_Foundation_initio_Predicate()
    Test_Foundation_initio_Class()
    Test_Foundation_initio_Object()
    Test_Foundation_initio_BelongTo()

    Test_Foundation_logic_Negation()
    Test_Foundation_logic_Conjunction()
    Test_Foundation_logic_Disjunction()
    Test_Foundation_logic_Implication()

    Test_Foundation_set_Subclass()
    Test_Foundation_set_Set()
    Test_Foundation_set_Element()
    Test_Foundation_set_SetEqual()


if __name__ == "__main__":

    TestRun()

# End of Test Operating File of UnivMathSys
