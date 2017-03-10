# Definition of Basic Set Theory for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.set of UnivMathSys'''


from Elementary.error import IllDefined, AccessError,\
    ProofNeeded
from Elementary.certify import Check
from Interpreter.enter import Verify
from Interpreter.resolver import ResolveEngine
from Foundation.basic import Variable, Operator, \
    Morphism
from Foundation.initio import Predicate, Class, \
    Object, BelongTo
from Foundation.logic import Neg, Imply


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


class Set(Variable):

    _Define = "Set"
    _Symbol = "X"
    _Element = "x"

    _Identify = r'(?:{|\\{)\s*' + \
                    r'(?P<Elmnt>.+?)\s*' +\
                    r'(?:\\in\s+(?P<Base>.+))?\s*' + \
                r'(?:\||\\mid\s)\s*' + \
                    r'(?P<Property>.+?)' + \
                r'(?:}|\\})'

    @Variable.UniqueInit
    def Initio(self):
        self._Symbol = self.GenUUID()
        self._Element = lambda any: \
            "_x" + hex(abs(hash(self._Symbol)))
        self._Condition = None
        self._Unique['Claim'] = lambda self: \
            self._Element(self)
        self._Unique['Property'] \
            = Predicate()
        self._Unique['Property'].Format = lambda any:\
            self._Element(self) + "\\in " + \
                self._Symbol
        self._Unique['Property'].Short = lambda any:\
            self._Unique['Property'].Format
        self._Unique['Property'].Condition \
            = self.Default
        self._Unique['Sync'] = False
        self._Unique['Base'] = False
        self._Format = lambda self: "\\{" + \
            self._Unique['Claim'](self) + "\\mid " + \
            self._Unique['Property'].Short("") + "\\}"

    @property
    def Elmnt(self):
        return self._Element(self)

    @Elmnt.setter
    def Elmnt(self, NewElm):
        self._Element = NewElm
        if not callable(NewElm):
            self._Element = lambda self: NewElm

    @property
    def Bases(self):
        return self._Unique['Depend']

    @Bases.setter
    def Bases(self, NewBase):
        if self._Unique['Base'] is False:
            self._Unique['Base'] = True
            self._Unique['Claim'] = lambda self: \
                self._Element(self) + "\\in " + \
                str(self._Unique['Depend'])
        Check(NewBase, Set)
        self._Unique['Depend'].append(NewBase)

    @staticmethod
    def Default(InVar, InSet):
        if InSet.Symbol in InVar.Status:
            return True
        if InSet.Condition:
            try: return InSet._Condition(InVar, InSet)
            except Exception: pass
        Status = [Set.Replace(InVar.Symbol, "_",
            Stats) for Stats in InVar.Status]
        if Status: Status[0] = "_\\in " + Status[0]
        Property = Set.Replace(InSet.Elmnt, "_",
            InSet.Property)
        Resolve = ResolveEngine.Resolve
        try: return Resolve(Status, Property)
        except ProofNeeded: return False

    @staticmethod
    def DefCheck(Input):
        Check(Input, Set)
        TempVar = Predicate()
        if Input.Inspect(TempVar, Input):
            print("Set Property Invalid: " + \
                "Probable Russell Set")
            raise IllDefined

    @property
    def Inspect(self):
        return self._Unique['Property'].Condition

    @property
    def Property(self):
        return self._Unique['Property'].Format

    @property
    def Condition(self):
        return self._Condition

    @Property.setter
    def Property(self, NewForm):
        TempForm = self.Property
        self._Unique['Property'].Format = NewForm
        self._Unique['Property'].Syntax, \
            self._Unique['Property'].BsList = \
                ResolveEngine.Generate\
                    (self._Unique['Property'].Format)
        try: Set.DefCheck(self)
        except IllDefined:
            self._Unique['Property'].Format = TempForm

    @Condition.setter
    def Condition(self, NewFunc):
        Check(NewFunc, 'function')
        TempFunc = self.Condition
        self._Condition = NewFunc
        try: Set.DefCheck(self)
        except IllDefined:
            self._Condition = TempFunc


class Element(Variable):

    _Define = "Element"
    _Symbol = "x"
    _Format = _Symbol

    _Identify = \
        r'(?P<Symbol>[a-zA-Z][0-9a-zA-Z\_]*)'

    @Variable.UniqueInit
    def Initio(self, InSet, InVar=None):
        self.Symbol = self.GenUUID()
        if InVar is not None:
            Check(InVar, Variable)
            self.Symbol = InVar.Symbol
            self.Unique = InVar.Unique
        if 'Element' in InSet.Unique:
            self.Format = InSet.Unique['Element']
        Check(InSet, Set)
        self.Status = lambda self: InSet.Symbol
        if InSet._Unique['Property']\
                .Unique['Sync'] is False:
            self.Status = lambda self: \
                self.Replace(InSet.Elmnt, \
                    self.Symbol, InSet.Property)

    def BelongTo(self, InSet):
        TempPredicate = Predicate()
        Check(InSet, Set)
        TempPredicate.Format = \
            self.Symbol + \
            "\\in" + " " + \
            InSet.Symbol
        TempPredicate.Truth = \
            InSet.Inspect(self, InSet)
        return TempPredicate


class Subset(Operator):

    _Define = "Subset"
    _Symbol = "\\subset"

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Set)
        Check(Rght, Set)
        TempPredicate.Format = \
            Left.Symbol + \
            self.Symbol + " " + \
            Rght.Symbol
        TempPredicate.Truth = Imply(
                Element(Left).BelongTo(Left), \
                Element(Left).BelongTo(Rght) \
            ).Truth
        return TempPredicate


class SetEqual(Operator):

    _Define = "equal"
    _Symbol = {False:"\\neq ", True:"="}

    @staticmethod
    def Action(self, Left, Rght):
        TempPredicate = Predicate()
        Check(Left, Set)
        Check(Rght, Set)
        Op = Subset()
        TempPredicate.Truth = \
            Op(Left, Rght).Truth \
            and Op(Rght, Left).Truth
        TempPredicate.Format = \
            Left.Symbol + \
            self.Symbol[TempPredicate.Truth] + \
            Rght.Symbol
        return TempPredicate


# End of Module Foundation.set of UnivMathSys
