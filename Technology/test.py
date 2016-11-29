# TestRun File of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Test Operating File of UnivMathSys'''


from Foundation.basic import MathBasic
from Elementary.build import TrueFunc
from Foundation.initio import Variable, Predicate,\
    Class, Object, BelongTo


def Test_Foundation_initio_Variable():

    print("Test of Variable:")
    TestVar = Variable()
    TestVar.Symbol = "\\varphi"
    TestVar.Rpsnt = "Test String"
    print(TestVar.Define)
    print(TestVar.Symbol)
    print(TestVar.MathForm)
    print(TestVar.Rpsnt)


def Test_Foundation_initio_Predicate():

    print("Test of Predicate")
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

    print("Test of Class")

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

    print("Test of Object")

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

    print("Test of BelongTo")

    Belongto = BelongTo()
    TestObject = Object()
    TestObjectF = Object()
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
    TestObject.ClsForm = TestClass

    print(Belongto.Define)
    print(Belongto.Symbol)
    print(BelongTo.BelongsTo(TestObject, TestClass).TruthValue)
    print(BelongTo.BelongsTo(TestObjectF, TestClass).TruthValue)


def TestRun():

    Test_Foundation_initio_Variable()
    Test_Foundation_initio_Predicate()
    Test_Foundation_initio_Class()
    Test_Foundation_initio_Object()
    Test_Foundation_initio_BelongTo()

if __name__ == "__main__":

    TestRun()

# End of Test Operating File of UnivMathSys
