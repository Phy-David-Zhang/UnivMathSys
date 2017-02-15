# TestRun File of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Test Operating File of UnivMathSys'''


from Foundation.basic import Variable, Operator, \
    Morphism
from Elementary.build import TrueFunc, FalseFunc
from Elementary.certify import Check
from Foundation.initio import Predicate, Class, \
    Object, BelongTo
from Foundation.logic import ForAll, Exist, Neg, \
    Conjunc, Disjunc, Imply
from Foundation.set import Subclass, Set, Element, \
    SetEqual
from Foundation.setop import Contain, SetEq, Union, \
    Intsct, Complt, CartProct


def Test_Foundation_initio_Predicate():

    print("\nTest of Predicate")
    TestPredicate = Predicate()
    TestPredicate.Symbol = "\\xi"
    TestPredicate.Truth = True
    TestPredicate.Condition = TrueFunc
    print(TestPredicate.Define, TestPredicate.Symbol,\
        TestPredicate.Format, TestPredicate.Truth, \
        TestPredicate.Condition())


def Test_Foundation_initio_Class():

    print("\nTest of Class")

    TestClass = Class()
    TestPredicate = Predicate()

    TestPredicate.Symbol = "P(y)"
    TestPredicate.Condition = TrueFunc

    TestClass.Symbol = "Y"
    TestClass.Object = "y"
    TestClass.Unique = dict(Property=TestPredicate)

    print(TestClass.Define, TestClass.Symbol, \
        TestClass.Format, \
        TestClass.Unique['Property'].Condition())


def Test_Foundation_initio_Object():

    print("\nTest of Object")

    TestClass = Class()
    TestPredicate = Predicate()

    TestPredicate.Symbol = "P(y)"
    TestPredicate.Condition = TrueFunc

    TestClass.Symbol = "Y"
    TestClass.Object = "y"
    TestClass.Unique = dict(Property=TestPredicate)

    TestObject = Object(TestClass)
    TestObject.Symbol = "y"

    print(TestObject.Define, TestObject.Symbol, \
        TestObject.Format, TestObject.Status, \
        TestObject.BelongTo(TestClass).Format, \
        TestObject.BelongTo(TestClass).Truth)


def Test_Foundation_initio_BelongTo():

    print("\nTest of BelongTo")

    def TestFunc(InVar, InClass):
        return InClass.Symbol in InVar.Status

    TestClass = Class()
    TestPredicate = Predicate()

    TestPredicate.Symbol = "P(y)"
    TestPredicate.Condition = TestFunc

    TestClass.Symbol = "Y"
    TestClass.Object = "y"
    TestClass.Unique = dict(Property=TestPredicate)

    TestObject = Object(TestClass)
    TestObject.Symbol = "y"

    In = BelongTo()

    print(In(TestObject, TestClass).Format, \
        In(TestObject, TestClass).Truth)


def Test_Foundation_logic_Quantifiers():

    print("\nTest of Quantifiers")

    TestClass = Class()

    ForAll(TestClass)
    print("Value: ", 'Value' in TestClass.Unique)

    Exist(TestClass)
    print("Value: ", 'Value' in TestClass.Unique)

    ForAll(TestClass)
    print("Value: ", 'Value' in TestClass.Unique)


def Test_Foundation_logic_Negation():

    print("\nTest of Negation")

    TestPredicate = Predicate()
    print(TestPredicate.Format, TestPredicate.Truth)
    print(Neg(TestPredicate).Format, \
          Neg(TestPredicate).Truth)


def Test_Foundation_logic_Conjunction():

    print("\nTest of Conjunction")

    TestPredicateA = Predicate()
    TestPredicateB = Predicate()

    TestPredicateA.Truth = True
    TestPredicateB.Symbol = "\\varphi"
    Result = Conjunc(TestPredicateA, TestPredicateB)

    print(Result.Format, Result.Truth)

    TestPredicateB.Truth = True
    Result = Conjunc(TestPredicateA, TestPredicateB)

    print(Result.Format, Result.Truth)


def Test_Foundation_logic_Disjunction():

    print("\nTest of Disjunction")

    TestPredicateA = Predicate()
    TestPredicateB = Predicate()

    TestPredicateA.Truth = True
    TestPredicateB.Symbol = "\\varphi"
    Result = Disjunc(TestPredicateA, TestPredicateB)

    print(Result.Format, Result.Truth)

    TestPredicateB.Truth = True
    Result = Disjunc(TestPredicateA, TestPredicateB)

    print(Result.Format, Result.Truth)


def Test_Foundation_logic_Implication():

    print("\nTest of Implication")

    TestPredicateA = Predicate()
    TestPredicateB = Predicate()

    TestPredicateB.Symbol = "\\varphi"

    Result = Imply(TestPredicateA, TestPredicateB)
    print(Result.Format, Result.Truth)

    TestPredicateA.Truth = True
    Result = Imply(TestPredicateA, TestPredicateB)

    print(Result.Format, Result.Truth)

    TestPredicateB.Truth = True
    Result = Imply(TestPredicateA, TestPredicateB)

    print(Result.Format, Result.Truth)


def Test_Foundation_set_Subclass():

    print("\nTest of Subclass")

    TestClass = Class()
    TestPredicate = Predicate()

    def TempFunc(InVar, InClass):
        return InClass.Symbol in InVar.Status

    TestPredicate.Symbol = "P(y)"
    TestPredicate.Condition = TempFunc

    TestClass.Symbol = "Y"
    TestClass.Object = "y"
    TestClass.Unique = dict(Property=TestPredicate)

    OpContain = Subclass()
    TempPredicate = OpContain.Action(OpContain,
        TestClass, TestClass)

    print(TempPredicate.Format, TempPredicate.Truth)


def Test_Foundation_set_Set():

    print("\nTest of Set")

    TempSet = Set()

    print(TempSet.Define, TempSet.Symbol, \
            TempSet.Format)

    def RussellCondition(InVar, InSet):
        Check(InVar, Variable)
        Check(InSet, Set)
        return not InSet.Symbol in InVar.Status

    TempSet.PropForm = "x\\notin X"
    TempSet.Condition = RussellCondition

    print(TempSet.Define, TempSet.Symbol, \
            TempSet.Format)

    TempSet.PropForm = "true"
    TempSet.Condition = TrueFunc

    print(TempSet.Define, TempSet.Symbol, \
            TempSet.Format)


def Test_Foundation_set_Element():

    print("\nTest of Element")

    TestSet = Set()

    TestSet.Symbol = "Y"
    TestSet.Object = "y"
    TestSet.PropForm = "P(y)"

    TestElmnt = Element(TestSet)

    print(TestElmnt.Define, TestElmnt.Symbol,
        TestElmnt.Format, TestElmnt.Status)

    TestElmnt.Format = "y\in Y"
    TempPredicate = TestElmnt.BelongTo(TestSet)

    print(TestElmnt.Format, TempPredicate.Format,
        TempPredicate.Truth)


def Test_Foundation_set_SetEqual():

    print("\nTest of SetEqual")

    TestSetA = Set()
    TestSetB = Set()
    TestPredicate = Predicate()

    def TempFunc(InVar, InSet):
        return InSet.Symbol in InVar.Status

    TestPredicate.Symbol = "P(y)"
    TestPredicate.Condition = TempFunc

    TestSetA.Symbol = "Y"
    TestSetA.Object = "y"
    TestSetA.Unique = dict(Property=TestPredicate)

    OpEqual = SetEqual()

    TempPredicate = \
        OpEqual.Action(OpEqual, TestSetA, TestSetA)
    print(TempPredicate.Format, TempPredicate.Truth)

    TempPredicate = \
        OpEqual.Action(OpEqual, TestSetA, TestSetB)
    print(TempPredicate.Format, TempPredicate.Truth)


def Test_Foundation_setop_Union():

    print("\nTest of Union")

    SetA = Set()
    SetB = Set()

    SetA.Symbol = "A"
    SetB.Symbol = "B"

    SetA.Elmnt = "a"
    SetB.Elmnt = "b"

    SetA.PropForm = "P(a)"
    SetB.PropForm = "P(b)"

    SetX = Union(SetA, SetB)
    Elmx = Element(SetX)

    print(SetX.Symbol, SetX.Unique['Origin'](SetX),
        SetX.Format)
    print(SetX.Unique)
    print(Elmx.Symbol, Elmx.Status)


def Test_Foundation_setop_Intsct():

    print("\nTest of Intersection")

    SetA = Set()
    SetB = Set()

    SetA.Symbol = "A"
    SetB.Symbol = "B"

    SetA.Elmnt = "a"
    SetB.Elmnt = "b"

    SetA.PropForm = "P(a)"
    SetB.PropForm = "P(b)"

    SetA.Condition = lambda InVar, InSet: \
        InSet.Symbol in InVar.Status
    SetB.Condition = lambda InVar, InSet: \
        InSet.Symbol in InVar.Status

    SetX = Intsct(SetA, SetB)
    Elmx = Element(SetX)

    print(SetX.Symbol, SetX.Unique['Origin'](SetX),
        SetX.Format)
    print(Elmx.Symbol, Elmx.Status)


def Test_Foundation_setop_Complt():

    print("\nTest of Complement")

    SetU = Set()
    SetA = Set()

    SetU.Symbol = "U"
    SetA.Symbol = "A"

    SetU.Object = "u"
    SetA.Object = "a"

    SetU.PropForm = "P(u)"
    SetA.PropForm = "P(a)"

    SetX = Complt(SetU, SetA)
    Elmx = Element(SetX)

    print(SetX.Symbol, SetX.Unique['Origin'](SetX),
        SetX.Format)
    print(Elmx.Symbol, Elmx.Status)


def Test_Foundation_setop_CartProct():

    print("\nTest of Cartesian Product")

    SetA = Set()
    SetB = Set()

    SetA.Symbol = "A"
    SetB.Symbol = "B"

    SetA.Elmnt = "a"
    SetB.Elmnt = "b"

    SetA.PropForm = "P(a)"
    SetB.PropForm = "P(b)"

    SetX = CartProct(SetA, SetB)
    Elmx = Element(SetX)

    print(SetX.Symbol, SetX.Unique['Origin'](SetX),
        SetX.Format)
    print(Elmx.Symbol, Elmx.Format, Elmx.Status)


def TestRun():

    print(" ")
    print("Test for Universal Mathematics System")

    Test_Foundation_initio_Predicate()
    Test_Foundation_initio_Class()
    Test_Foundation_initio_Object()
    Test_Foundation_initio_BelongTo()

    Test_Foundation_logic_Quantifiers()
    Test_Foundation_logic_Negation()
    Test_Foundation_logic_Conjunction()
    Test_Foundation_logic_Disjunction()
    Test_Foundation_logic_Implication()

    Test_Foundation_set_Subclass()
    Test_Foundation_set_Set()
    Test_Foundation_set_Element()
    Test_Foundation_set_SetEqual()

    Test_Foundation_setop_Union()
    Test_Foundation_setop_Intsct()
    Test_Foundation_setop_Complt()
    Test_Foundation_setop_CartProct()


if __name__ == "__main__":

    TestRun()

# End of Test Operating File of UnivMathSys
