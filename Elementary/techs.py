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

    def __str__(self):
        return self.GetInfo(self)

    def __repr__(self):
        return self.GetRepr(self)

    def Initio(self, *args, **kwargs):
        pass

    @staticmethod
    def Update(self):
        pass

    @staticmethod
    def Action(self, *args):
        pass

    @staticmethod
    def GetInfo(self):
        pass

    @staticmethod
    def GetRepr(self):
        pass

# End of Module Elementary.Techs of UnivMathSys
