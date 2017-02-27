# Language Compiler of Universal Mathematics System

    # Copyright (C) 2016 Zhang Chang-kai #
    # Contact via: phy.zhangck@gmail.com #
    # General Public License version 3.0 #

'''Interface Language Compiler of UnivMathSys'''


import re
from .exeinit import ExeInit
from .analyser import Analyse


# Form: let ... be ...
LetBeForm = r'let\s+(.*)\s+be\s+(\w*)\s*'
# Form: let ... be ... of ...
LetBeOfForm = \
    r'let\s+(.*)\s+be\s+(\w*)\s+of\s+(\w*)\s*'
# Form: let ... of ... be ...
LetOfBeForm = \
    r'let\s+(\w*)\s+of\s+(.*)\s+be\s+([.*\s*]*.+)'

# compile syntax
LetBeSyntax = re.compile(LetBeForm)
LetBeOfSyntax = re.compile(LetBeOfForm)
LetOfBeSyntax = re.compile(LetOfBeForm)

# Assignment Form: defined as :=
DefinedAsForm = r'(.*\w+)\s*:=\s*(.*)'
DefinedAsSyntax = re.compile(DefinedAsForm)


# compile given sentences
def Compile(sntces):

    # if match 'let ... of ... be ...' form
    if re.match(LetOfBeForm, sntces):
        Info = LetOfBeSyntax.match(sntces).groups()
        # extract names
        Info = [re.split(r'[\s\,]+', Info[1])]\
            + [Info[0]] + [info for info in Info[2:]]
        # generate commands
        Command = ""
        for Name in Info[0]:
            Command += Name + "." + Info[1] + "=" \
                + Info[2] + "\n"
        return Command

    # if match 'let ... be ... of ...' form
    elif re.match(LetBeOfForm, sntces):
        Info = LetBeOfSyntax.match(sntces).groups()
        # extract names
        Info = [re.split(r'[\s\,]+', Info[0])]\
            + [info for info in Info[1:]]
        # generate commands
        Command = ""
        for Name in Info[0]:
            # create instance
            Command += Name + "=" + Info[1] \
                + "(" + Info[2] + ")\n"
            # set symbol of instance
            Command += Name + ".Symbol='" \
                + Name + "'\n"
            # other initialization
            Temp = ExeInit(Name, Info[1])
            if Temp:
                Command += Temp
        return Command

    # if match 'let ... be ...' form
    elif re.match(LetBeForm, sntces):
        Info = LetBeSyntax.match(sntces).groups()
        # extract names
        Info = [re.split(r'[\s\,]+', Info[0])]\
            + [info for info in Info[1:]]
        # generate commands
        Command = ""
        for Name in Info[0]:
            # create instance
            Command += Name + "=" + Info[1] + "()\n"
            # set symbol of instance
            Command += Name + ".Symbol='" \
                + Name + "'\n"
            # other initialization
            Temp = ExeInit(Name, Info[1])
            if Temp:
                Command += Temp
        return Command

    # if match ':=' form
    elif re.match(DefinedAsForm, sntces):
        Info = DefinedAsSyntax.match(sntces).groups()
        # extract names
        NameList = re.split(r'[\s\,]+', Info[0])
        Definition = Info[1]
        # generate commands
        Command = ""
        for Name in NameList:
            Command += Analyse(Name, Definition,
                flag='Command')
        return Command

    # return None if match fails
    else:
        return None


# End of Compiler of UnivMathSys
