# Techniques on Interface with Computer Language

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Module Elementary.Techs of UnivMathSys'''

class Techniques(object):

    def __init__(self, *args, **kwargs):
        self.Initio(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.Action(self, *args, **kwargs)

    @staticmethod
    def Update(self):
        pass

    def Initio(self):
        pass

    @staticmethod
    def Action(self, *args):
        pass

# End of Module Elementary.Techs of UnivMathSys
