# Initialization Prepared for Run in UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Initialization for Run in UnivMathSys'''


from UnivMathSys import *

def ExeInit(Var, Type):

    if getattr(Var, 'ExeInitio', None):
        return Var.ExeInitio()
    else:
        FuncName = Type + "_ExeInitio"
        try:
            cmd = eval(FuncName + "(Var)")
            return cmd
        except NameError:
            pass

def Class_ExeInitio(Var):
    return Var + ".Object=" + Var + \
        ".Symbol.lower()\n"

def Set_ExeInitio(Var):
    return Var + ".Elmnt=" + Var + \
        ".Symbol.lower()\n"


# End of Initialization for Run in UnivMathSys
