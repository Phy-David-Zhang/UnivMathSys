# Mathematical Language Analyser of UnivMathSys

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Maths Language Analyser of UnivMathSys'''


import re
import logging
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

    # default: extract all info from a string
    if flag is None:
        Info = Match(args[0])
        return Info

    # analyse type of input
    elif flag is 'Type':
        Info = Match(args[0], flag='Type')
        return Info[0]

    # provide certification of two predicates
    elif flag is 'Certify':
        pass

    # generate python commands for input
    elif flag is 'Command':
        # try generating if input is among basic forms
        try:
            Info = Match(args[1])
            Info.update(Name=args[0])
            return Generate(Info)
        except MatchError:
            Formula = None
            Info = dict(Name=args[0])
            for ast, type in GeneralFormulas.items():
                try:
                    Formula = ast.Analyse(args[1])
                    Info['Type'] = type
                    Info['Formula'] = Formula
                except Exception:
                    if type is 'Set':
                        logging.exception("")
            if not Formula:
                raise MatchError("Unable to match " +\
                    args[1] + " with all formulas")
            return Generate(Info,
                FormulaType='General')

    else:
        raise KeyError("Invalid Flag: " + flag)


def Match(Input, flag=None):

    # default: search basic formulas
    if flag is None:
        # compile syntax
        Syntax = {re.compile(key): value
            for key, value in BasicFormulas.items()}
        # try if input matches syntax
        for syn, type in Syntax.items():
            # if match, return a dict containing info
            if syn.match(Input):
                data = dict(Type=type)
                data.update(syn.match(Input)\
                    .groupdict())
                return data

        raise MatchError("Unable to match " + Input +\
            " with basic formulas")

    # search basic and general formulas to find type
    elif flag is 'Type':
        # try match in basic fomulas
        try: return Match(Input)['Type']
        except MatchError:
            pass
        # try match in general formulas
        for ast, type in GeneralFormulas.items():
            if ast.Analyse(Input):
                return type
        raise MatchError("Unable to match " + Input +\
            " with all build-in formulas")

    else:
        raise KeyError("Invalid Flag: " + flag)


# generate python codes
def Generate(Info, FormulaType='Basic'):

    Type = Info['Type']
    Name = Info['Name']

    if Type is 'Identifier' and \
                FormulaType is 'Basic':
        Command = Name + "=" + Info['ID'] + "\n"
        Command += Name + ".Symbol='" + Name + "'\n"
        return Command

    if FormulaType is 'Basic':
        Command = Name + "=" + Type + "()\n"
    elif FormulaType is 'General':
        Command = Name + "=" + Info['Formula'] + "\n"
    else:
        raise KeyError("Unknown Formula Type")

    Command += Name + ".Symbol='" + Name + "'\n"

    if Type is 'Predicate' and FormulaType is 'Basic':
        Command += Name + ".Format=" + \
            "'" + Info['Form'] + "'\n"

    if Type is 'Set' and FormulaType is 'Basic':
        Command += Name + ".Elmnt=" + \
            "'" + Info['Elmnt'] + "'\n"
        Command += Name + ".Property=" + \
            "'" + Info['Property'] + "'\n"
        if Info['Base']:
            Command += Name + ".Base=" + \
                "'" + Info['Base'] + "'\n"

    if Type is 'Set' and FormulaType is 'General':
        Command += "if " + Name + ".Elmnt" + \
            ".startswith('_'): \n"
        Command += "    " + Name + ".Elmnt=" + \
            Name + ".Symbol.lower()\n"

    return Command


# End of Language Analyser of UnivMathSys
