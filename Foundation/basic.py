# Fundamental Mathematical Terms for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.basic of UnivMathSys'''


from Elementary.techs import Techniques


class Variable(Techniques):

    '''Base Class of Variable'''

    _Define = None
    _Symbol = None
    _Unique = None

    @property
    def Define(self):
        return self._Define

    @property
    def Symbol(self):
        return self._Symbol

    @property
    def Unique(self):
        return self._Unique

    @Symbol.setter
    def Symbol(self, NewSym):
        self._Symbol = NewSym

    @Unique.setter
    def Unique(self, NewUnq):
        self._Unique = NewUnq


class Operator(Techniques):

    '''Base Class of Operator'''

    _Define = None
    _Symbol = None

    @property
    def Define(self):
        return self._Define

    @property
    def Symbol(self):
        return self._Symbol

    @staticmethod
    def Action(self, *args):
        pass


class Morphism(Techniques):

    '''Base Class of Morphism'''

    _Define = None
    _Symbol = None

    @property
    def Define(self):
        return self._Define

    @property
    def Symbol(self):
        return self._Symbol

    @staticmethod
    def Action(self, *args):
        self.Functor(*args)

    @staticmethod
    def Functor(self, *args):
        pass


# End of Module Foundation.basic of UnivMathSys
