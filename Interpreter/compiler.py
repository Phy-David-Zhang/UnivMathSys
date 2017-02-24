# Language Compiler of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Interface Language Compiler of UnivMathSys'''


import re


LetBeForm = r'let\s+(\w*)\s+be\s+(\w*)\s*'
LetBeOfForm = \
    r'let\s+(\w*)\s+be\s+(\w*)\s+of\s+(\w*)\s*'
LetOfBeForm = \
    r'let\s+(\w*)\s+of\s+(\w*)\s+be\s+(\w*)\s*'

LetBeSyntax = re.compile(LetBeForm)
LetBeOfSyntax = re.compile(LetBeOfForm)
LetOfBeSyntax = re.compile(LetBeOfForm)


def Compile(sntces):

    if re.match(LetBeOfForm, sntces):
        Info = LetOfBeSyntax.match(sntces).groups()
        Command = Info[0] + "=" + Info[1] + "(" \
            + Info[2] + ")\n"
        return Command

    elif re.match(LetBeForm, sntces):
        Info = LetBeSyntax.match(sntces).groups()
        Command = Info[0] + "=" + Info[1] + "()\n"
        return Command

    elif re.match(LetOfBeForm, sntces):
        Info = LetOfBeSyntax.match(sntces).groups()
        Command = Info[1] + "." + Info[0] + "=" \
            + Info[2] + "\n"
        return Command
    else:
        return None


# End of Compiler of UnivMathSys
