# Fundamental Mathematical Terms for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.basic of UnivMathSys'''


from Elementary.techs import Techniques
from functools import wraps


class Variable(Techniques):

    '''Base Class of Variable'''

    _Define = "Variable"
    _Symbol = None
    _Format = None
    _Unique = dict()

    @classmethod
    def UniqueInit(cls, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self._Unique = dict(
                Depend = list(),
                Status = list(),
                Sync = True)
            self._Format = \
                lambda self: self._Symbol
            func(self, *args, **kwargs)
        return wrapper

    @staticmethod
    def GetInfo(self):
        return self.Symbol + "=" + self.Format

    @staticmethod
    def GetRepr(self):
        return self.Format

    @property
    def Define(self):
        return self._Define

    @property
    def Symbol(self):
        return self._Symbol

    @property
    def Format(self):
        return self._Format(self)

    @property
    def Unique(self):
        return self._Unique

    @property
    def Status(self):
        return [Stats(self) for
            Stats in self._Unique['Status']]

    @Symbol.setter
    def Symbol(self, NewSym):
        self._Symbol = NewSym

    @Format.setter
    def Format(self, NewExp):
        self._Unique['Sync'] = False
        self._Format = NewExp
        if not callable(NewExp):
            self._Format = lambda self: NewExp

    @Unique.setter
    def Unique(self, NewUnq):
        self._Unique.update(NewUnq)

    @Status.setter
    def Status(self, NewStat):
        self._Unique['Status'].append(NewStat)


class Operator(Techniques):

    '''Base Class of Operator'''

    _Define = None
    _Symbol = None

    @staticmethod
    def Action(self, *args, **kwargs):
        pass

    @property
    def Define(self):
        return self._Define

    @property
    def Symbol(self):
        return self._Symbol


class Morphism(Techniques):

    '''Base Class of Morphism'''

    _Define = None
    _Symbol = None
    _Format = None
    _Domain = None
    _Ranges = None

    @staticmethod
    def Action(self, *args):
        self.Functor(*args)

    @staticmethod
    def Functor(*args):
        pass

    @property
    def Define(self):
        return self._Define

    @property
    def Symbol(self):
        return self._Symbol

    @property
    def Format(self):
        return self._Format

    @property
    def Domain(self):
        return self._Domain

    @property
    def Ranges(self):
        return self._Ranges

    @Format.setter
    def Format(self, NewExp):
        self._Format = NewExp

    @Domain.setter
    def Domain(self, NewDom):
        self._Domain = NewDom

    @Ranges.setter
    def Ranges(self, NewRan):
        self._Ranges = NewRan


# End of Module Foundation.basic of UnivMathSys
