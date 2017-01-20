# Fundamental Mathematical Terms for UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Foundation.basic of UnivMathSys'''

from Elementary.techs import Techniques

class MathBasic(Techniques):

    '''Base Class of Maths'''

    Definition = None
    Denotation = None
    Formulation = None

    @property
    def Define(self):
        return self.Definition

    @property
    def Symbol(self):
        return self.Denotation

    @property
    def MathForm(self):
        return self.Formulation

    @Symbol.setter
    def Symbol(self, NewSym):
        self.Denotation = NewSym

    @MathForm.setter
    def MathForm(self, NewForm):
        self.Formulation = NewForm

# End of Module Foundation.basic of UnivMathSys
