# Mathematical Language Analyser of UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Maths Language Analyser of UnivMathSys'''


import re
from .formula import BasicFormulas, GeneralFormulas
from collections import namedtuple
from Elementary.error import MatchError


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
        Info = Match(args[0], flag='Type')
        return Info[0]

    elif flag is 'Certify':
        pass

    elif flag is 'Command':
        try:
            Info = Match(args[1])
            Info.update(Name=args[0])
            Command = Generate(Info)
            return Command
        except MatchError:
            pass

    else:
        raise KeyError("Invalid Flag: " + flag)


def Match(Input, flag=None):

    if flag is None:

        Syntax = {re.compile(key): value
            for key, value in BasicFormulas.items()}

        for syn, type in Syntax.items():
            if syn.match(Input):
                data = dict(Type=type)
                data.update(syn.match(Input)\
                    .groupdict())
                return data

        raise MatchError("Unable to match " + Input +\
            " with basic formulas")

    elif flag is 'Type':

        try: return Match(Input)['Type']
        except MatchError:
            pass

        for ast, type in GeneralFormulas.items():
            if ast.Analyse(Input):
                return type
        raise MatchError("Unable to match " + Input +\
            " with all build-in formulas")

    else:
        raise KeyError("Invalid Flag: " + flag)


def Generate(Info):

    Type = Info['Type']
    Name = Info['Name']

    if Type is "Predicate":
        Command = Name + "=Predicate()\n"
        Command += Name + ".Symbol='" + Name + "'\n"
        Command += Name + ".Format=" + \
            "'" + Info['Form'] + "'\n"

    if Type is "Set":
        Command = Name + "=Set()\n"
        Command += Name + ".Symbol='" + Name + "'\n"
        Command += Name + ".Elmnt=" + \
            "'" + Info['Elmnt'] + "'\n"
        Command += Name + ".Property=" + \
            "'" + Info['Property'] + "'\n"
        if Info['Base']:
            Command += Name + ".Base=" + \
                "'" + Info['Base'] + "'\n"

    return Command


# End of Language Analyser of UnivMathSys
