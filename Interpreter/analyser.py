# Mathematical Language Analyser of UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Maths Language Analyser of UnivMathSys'''


import re
from .formula import Formulas


# ----------------------------
#    Analyse Maths Formula
# ----------------------------
#  flag   |        args
# ----------------------------
#  None   |       String
#  Type   |       String
# Certify | [Status, Property]
# Command | [Name, Definition]
# ----------------------------
# Info -> [Type, Name, ...]
# ----------------------------

def Analyse(*args, flag=None):

    if flag is None:
        Info = Match(args[0])
        return Info

    elif flag is 'Type':
        Info = Match(args[0])
        return Info[0]

    elif flag is 'Certify':
        pass

    elif flag is 'Command':
        Info = Match(args[1])
        Info.insert(1, args[0])
        Command = Generate(Info)
        return Command

    else:
        raise KeyError("Invalid Key: " + flag)


def Match(Input):

    Syntax = {re.compile(key): value
        for key, value in Formulas.items()}

    for key, value in Syntax.items():
        if key.match(Input):
            data = key.match(Input).groups()
            data = [d for d in data if d is not None]
            data.insert(0, value)
            return data

    raise SyntaxError("Invalid Syntax: " + Input)


def Generate(Info):

    Type = Info.pop(0)
    Name = Info.pop(0)

    if Type is "Predicate":
        Command = Name + "=" + Type + "()\n"
        Command += Name + ".Symbol='" + Name + "'\n"
        Command += Name + ".Format=" + Info[0] + "\n"

    if Type is "Logic":
        Command = Name + "=" + Info[0] + "\n"
        Command += Name + ".Symbol='" + Name + "'\n"

    if Type is "Class":
        Command = Name + "=" + Type + "()\n"
        Command += Name + ".Symbol='" + Name + "'\n"
        Command += Name + ".Object=" + Info[0] + "\n"
        Command += Name + \
            ".Unique['Property'].Format=" + Info[1] \
            + "\n"

    if Type is "Set":
        Command = Name + "=" + Type + "()\n"
        Command += Name + ".Symbol='" + Name + "'\n"
        Command += Name + ".Elmnt=" + \
            "'" + Info[0] + "'\n"
        Command += Name + ".PropForm=" + \
            "'" + Info[1] + "'\n"

    if Type is "SetOp":
        Command = Name + "=" + Info[0] + "\n"
        Command += Name + ".Symbol='" + Name + "'\n"
        Command += Name + ".Elmnt=" + Name + \
            ".Symbol.lower()\n"

    return Command


# End of Language Analyser of UnivMathSys
