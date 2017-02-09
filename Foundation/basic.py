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
                Status = list(),
                Sync = True)
            func(self, *args, **kwargs)
        return wrapper

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
    def Unique(self):
        return self._Unique

    @property
    def Status(self):
        return self._Unique['Status']

    @Symbol.setter
    def Symbol(self, NewSym):
        self._Symbol = NewSym
        self.Update(self)

    @Format.setter
    def Format(self, NewExp):
        self._Format = NewExp
        self.Update(self)

    @Unique.setter
    def Unique(self, NewUnq):
        self._Unique.update(NewUnq)
        self.Update(self)

    @Status.setter
    def Status(self, NewStat):
        self._Unique['Status']\
            .append(NewStat)
        self.Update(self)


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
        self.Update(self)

    @Domain.setter
    def Domain(self, NewDom):
        self._Domain = NewDom
        self.Update(self)

    @Ranges.setter
    def Ranges(self, NewRan):
        self._Ranges = NewRan
        self.Update(self)


# End of Module Foundation.basic of UnivMathSys
