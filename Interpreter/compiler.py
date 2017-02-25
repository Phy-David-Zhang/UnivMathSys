# Language Compiler of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Interface Language Compiler of UnivMathSys'''


import re
from .exeinit import ExeInit


LetBeForm = r'let\s+(.*)\s+be\s+(\w*)\s*'
LetBeOfForm = \
    r'let\s+(.*)\s+be\s+(\w*)\s+of\s+(\w*)\s*'
LetOfBeForm = \
    r'let\s+(\w*)\s+of\s+(.*)\s+be\s+([\w*\s*]*\w+)'

LetBeSyntax = re.compile(LetBeForm)
LetBeOfSyntax = re.compile(LetBeOfForm)
LetOfBeSyntax = re.compile(LetOfBeForm)


def Compile(sntces):

    if re.match(LetOfBeForm, sntces):
        Info = LetOfBeSyntax.match(sntces).groups()
        Info = [re.split(r'[\s\,]+', Info[1])]\
            + [Info[0]] + [info for info in Info[2:]]
        Command = ""
        for Name in Info[0]:
            Command += Name + "." + Info[1] + "='" \
                + Info[2] + "'\n"
        return Command

    elif re.match(LetBeForm, sntces):
        Info = LetBeSyntax.match(sntces).groups()
        Info = [re.split(r'[\s\,]+', Info[0])]\
            + [info for info in Info[1:]]
        Command = ""
        for Name in Info[0]:
            Command += Name + "=" + Info[1] + "()\n"
            Command += Name + ".Symbol='" \
                + Name + "'\n"
            Temp = ExeInit(Name, Info[1])
            if Temp:
                Command += Temp
        return Command

    elif re.match(LetBeOfForm, sntces):
        Info = LetBeOfSyntax.match(sntces).groups()
        Info = [re.split(r'[\s\,]+', Info[0])]\
            + [info for info in Info[1:]]
        Command = ""
        for Name in Info[0]:
            Command += Name + "=" + Info[1] \
                + "(" + Info[2] + ")\n"
            Command += Name + ".Symbol='" \
                + Name + "'\n"
            Temp = ExeInit(Name, Info[1])
            if Temp:
                Command += Temp
        return Command

    else:
        return None


# End of Compiler of UnivMathSys
